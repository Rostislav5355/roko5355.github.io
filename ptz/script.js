const firebaseConfig = {
  apiKey: "TVŮJ_API_KLÍČ",
  authDomain: "tvůj-projekt.firebaseapp.com",
  databaseURL: "https://tvůj-projekt.firebaseio.com",
  projectId: "tvůj-projekt",
};

firebase.initializeApp(firebaseConfig);
const db = firebase.database();

function send(cmd) {
  db.ref('camera/command').set(cmd);
}
