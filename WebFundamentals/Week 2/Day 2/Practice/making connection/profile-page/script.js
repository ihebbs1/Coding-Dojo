const acceptButton = document.querySelector(".connection-actions");
const imageElement = document.querySelector(".connection-image");
const badgeElement = document.querySelector(".connection-badge");
const acceptButton2 = document.querySelector(".connection-actions");
const imageElement2 = document.querySelector(".connection-image2");

function acceptRequest() {
    acceptButton.remove();
    imageElement.remove();
    badgeElement.innerText--;
}

function acceptRequest2() {
    acceptButton2.remove();
    imageElement2.remove();
    badgeElement.innerText--;
}

const userName = document.querySelector(".user-name");

function changeName() {
    userName.innerHTML = "Marlin Monoro";
}
