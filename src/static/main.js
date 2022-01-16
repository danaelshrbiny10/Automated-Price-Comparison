
cc=document.querySelectorAll("#rating_Val");

let ratings = {};
for (var i = 0; i < cc.length; i++) {
       ratings['rating' + i] =  parseFloat(document.querySelectorAll("#rating_Val")[i].innerText)
}
const starTotal = 5;
for(const rating in ratings) {  
  // 2
  const starPercentage = (ratings[rating] / starTotal) * 100;
  // 3
  const starPercentageRounded = `${(Math.round(starPercentage / 10) * 10)}%`;
  // 4
  document.querySelector(`.${rating} .stars-inner`).style.width = starPercentageRounded; }