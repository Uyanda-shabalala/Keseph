//js file to communicate with the expenses api
export function new_expense(data) {
  //expense function that takes in an object containing data from the form , reason for use: easier to manage than an array
  fetch("/api/addexpense", {
    method: "POST",
    headers: { "Content-type": "application/json" },
    body: JSON.stringify(data),
  }).then((res) => res.json());
}
