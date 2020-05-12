function loading (idItem, changeText=true) {
  document.getElementById(idItem).className += ' isDisabled'

  if (changeText) {
    document.getElementById(idItem).innerHTML =
      'Loading...'   
  }

  return true
}

function hideAlert (idAlert) {
  document.getElementById(idAlert).style.display = 'none'

  return true
}

function hideShowItem (idItem) {
  let itemDOM = document.getElementById(idItem)
  let buttonDOM = document.getElementById('b_' + idItem)

  if (itemDOM.style.display === 'none') {
    itemDOM.style.display = 'block'
    buttonDOM.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" style="fill:#a0aec0;"><path d="M0 16.67l2.829 2.83 9.175-9.339 9.167 9.339 2.829-2.83-11.996-12.17z"/></svg>'
  } else {
    itemDOM.style.display = 'none'
    buttonDOM.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" style="fill:#a0aec0;"><path d="M0 7.33l2.829-2.83 9.175 9.339 9.167-9.339 2.829 2.83-11.996 12.17z"/></svg>'
  }

  return true
}

function showInfo (textInf) {
  let modal = document.getElementById('info_modal')
  let text = document.getElementById('textInfo')

  modal.style.display = "block"
  textInfo.innerHTML = textInf

  return true
}

function closeInfo () {
  let modal = document.getElementById('info_modal')
  let text = document.getElementById('textInfo')

  modal.style.display = "none"
  textInfo.innerHTML = ""

  return true
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    let modal = document.getElementById('info_modal')

  if (event.target == modal) {
      let text = document.getElementById('textInfo')
      
      modal.style.display = "none"
      textInfo.innerHTML = ""
  }
}
