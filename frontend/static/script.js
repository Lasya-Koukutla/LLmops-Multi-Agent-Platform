async function sendPrompt() {

    const prompt = document.getElementById("user_input").value;

    if (prompt.trim() === "") {
        alert("Please enter a prompt.");
        return;
    }

    document.getElementById("validation").innerHTML =
        "✔ Validating Prompt...";

    document.getElementById("analysis").innerHTML =
        "✔ Analyzing Prompt...";

    document.getElementById("refined_prompt").innerHTML =
        "✔ Refining Prompt...";

    document.getElementById("execution_time").innerHTML = "";

    document.getElementById("response").innerHTML =
        "🤖 Generating Response...";

    const response = await fetch("/generate", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            prompt: prompt
        })

    });

    const data = await response.json();

    document.getElementById("validation").innerHTML =
        data.validation || "";

    document.getElementById("analysis").innerHTML =
        data.analysis || "";

    document.getElementById("refined_prompt").innerHTML =
        data.refined_prompt || "";

    document.getElementById("execution_time").innerHTML =
        data.execution_time || "";

    document.getElementById("response").innerHTML =
        data.response || "";
}


function clearOutput(){

    document.getElementById("user_input").value = "";

    document.getElementById("validation").innerHTML = "";

    document.getElementById("analysis").innerHTML = "";

    document.getElementById("refined_prompt").innerHTML = "";

    document.getElementById("execution_time").innerHTML = "";

    document.getElementById("response").innerHTML = "";

}


function copyResponse(){

    const text = document.getElementById("response").innerText;

    navigator.clipboard.writeText(text);

    alert("Response copied successfully!");

}


function downloadResponse(){

    const text = document.getElementById("response").innerText;

    const blob = new Blob([text], {type:"text/plain"});

    const link = document.createElement("a");

    link.href = URL.createObjectURL(blob);

    link.download = "Gemini_Response.txt";

    link.click();

}