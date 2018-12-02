(function(){
  const config = {
    apiKey: "AIzaSyCTveh2KmXDzkZZXQ3P0m_G6VW9P3bNjL0",
    authDomain: "first-server-169214.firebaseapp.com",
    databaseURL: "https://first-server-169214.firebaseio.com",
    projectId: "first-server-169214",
    storageBucket: "first-server-169214.appspot.com",
    messagingSenderId: "356121094177"
  };
  firebase.initializeApp(config);
  const preObject = document.getElementById('arbitrage');
  const dbRefObject = firebase.database().ref().child('arbitrage');
  dbRefObject.on('value', snap => console.log(snap.val()));
}());


