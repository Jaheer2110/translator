async function translateText() {
  const text = document.getElementById("inputText").value;
  const sourceLang = document.getElementById("sourceLang").value;
  const targetLang = document.getElementById("targetLang").value;

  const response = await fetch("http://127.0.0.1:5000/translate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      source_lang: sourceLang,
      target_lang: targetLang,
      text: text
    })
  });

  const data = await response.json();
  if (data.translation) {
    document.getElementById("outputBox").innerText = data.translation;
  } else {
    document.getElementById("outputBox").innerText = "Error: " + data.error;
  }
}
