function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }


function findAns(id, answer, question) {
  var myElement = document.getElementById(id);
  let utterance = new SpeechSynthesisUtterance(question);
  if (myElement.innerHTML == answer) {
    utterance.text = question
    speechSynthesis.speak(utterance);
    myElement.innerHTML = question
  }
  else{
    utterance.text = answer;
    speechSynthesis.speak(utterance);
    myElement.innerHTML = answer;
  }
  
}