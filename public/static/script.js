// sign up script

function validatePasswords() {
  const password = document.getElementById("password").value;
  const confirmPassword = document.getElementById("confirmPassword").value;

  if (password !== confirmPassword) {
    showError("Passwords do not match");
    return null;
  }

  return password;
}

function create_account() {
  const form = document.getElementById("signup-form");

  form.addEventListener("submit", function (event) {
    //listens for the submit event
    event.preventDefault(); //the preventDefault() can be added to any event to prevent its default behavior in this case it prevent the fomrs default behavior to send data to the server

    const firstname = document.getElementById("firstname").value;
    const surname = document.getElementById("surname").value;
    const password = validatePasswords();

    if (!password) return;

    const phone = document.getElementById("phone").value;
    const income = document.getElementById("income").value;
    const expenditure = document.getElementById("expenditure").value;
    const balance = document.getElementById("balance").value;
    const savings = document.getElementById("savings").value;

    fetch("api/createaccount", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        firstname: firstname,
        surname: surname,
        password: password,
        phone: phone,
        income: income,
        expenditure: expenditure,
        balance: balance,
        savings: savings,
      }),
    });
  });
}
