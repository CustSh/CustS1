const arrowButton = document.querySelector('.arrow-button');
function topFunction() {
  document.body.scrollTop = 0; 
  document.documentElement.scrollTop = 0; 
}


const notificationButton = document.querySelector('[aria-controls="notifications"]');
const notificationList = document.querySelector('#notifications');

notificationButton.addEventListener('click', () => {
  const notificationsOpened = notificationButton.getAttribute('aria-expanded') === 'true';

  notificationButton.setAttribute('aria-expanded', !notificationsOpened);
  if (notificationsOpened) {
    notificationList.style.height = '0'; 
    notificationList.style.visibility = 'hidden'; 
  } else {
    notificationList.style.height = 'auto'; 
    notificationList.style.visibility = 'visible'; 
  }
});
