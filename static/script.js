async function translateText() {
  const src = document.getElementById("sourceLang").value;
  const tgt = document.getElementById("targetLang").value;
  const inputText = document.getElementById("inputText").value.trim();
  const outputBox = document.getElementById("outputBox");

  if (!inputText) {
    alert("Please enter some text to translate.");
    return;
  }

  try {
    const response = await fetch("http://localhost:5000/translate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        source_lang: src,
        target_lang: tgt,
        text: inputText
      })
    });

    const data = await response.json();

    if (data.translation) {
      outputBox.innerHTML = `<strong>Translation:</strong><br>${data.translation}`;
      outputBox.style.display = "block";
    } else {
      outputBox.innerText = "Something went wrong.";
    }
  } catch (err) {
    console.error(err);
    outputBox.innerText = "Failed to fetch translation. Please check your server.";
    outputBox.style.display = "block";
  }
}
