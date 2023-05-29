//function serializeForm(formNode) {
//  const { elements } = formNode
//
//  const data = Array.from(elements)
//    .map((element) => {
//      const { type } = element
//      const value = (type === 'checkbox')? element.checked : (type === 'radio')? element.checked:element.value
//      const id = (type === 'checkbox') ? element.name : element.id
//      return { id, value }
//    })
//  console.log(data)
//}
//function handleFormSubmit(event) {
//  event.preventDefault()
//  serializeForm(applicantForm)
//}
//
//const applicantForm = document.getElementById('form')
//applicantForm.addEventListener('submit', handleFormSubmit)
//
///*const form = document.getElementById('form');
//
//form.addEventListener('submit', getFormValue);
//
//function getFormValue(event) {
//   event.preventDefault();
//   const name = form.querySelector('[name="name"]'), //получаем поле name
//         age = form.querySelector('[name="age"]'), //получаем поле age
//         gender = form.querySelector('[name="gender"]'), //получаем поле terms
//        data = {
//        name: name.value,
//        age: age.value,
//        gender: gender.checked
//   }
//};
//
//console.log(data);
//*/