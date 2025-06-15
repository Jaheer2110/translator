async function translateText() {
  const text = document.getElementById("inputText").value;
  const source = document.getElementById("sourceLang").value;
  const target = document.getElementById("targetLang").value;

  const res = await fetch("/translate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ text, source, target })
  });

  const data = await res.json();
  const outputBox = document.getElementById("outputBox");
  outputBox.style.display = "block";

  if (data.translated_text) {
    outputBox.innerText = data.translated_text;
  } else {
    outputBox.innerText = "Error: " + data.error;
  }
}
