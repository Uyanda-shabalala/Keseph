export function new_income(data) {
  //income function that takes in an object containing data from the form , reason for use: easier to manage than an array

  //purpose of function : to communicate with the api

  fetch("/api/addincome", {
    method: "POST",
    headers: { "Content-type": "application/json" },
    body: JSON.stringify(data),
  }).then((res) => res.json());
}
