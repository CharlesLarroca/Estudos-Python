function limesToCut(wedgesNeeded, limes) {
  let soma = 0
  let originalLength = limes.length
  console.log(originalLength)
  for (let i = soma; i <= wedgesNeeded; i++){
    for(let j = 0; j < limes.length[i]; j++){
      switch (limes){
          case 'small':
            limes.shift()
            soma += 6
            break;
          case 'medium':
            limes.shift()
            soma += 8
            break;
          case 'large':
            limes.shift()
            soma += 10
            break;
      }
      return (soma)  
    }
    console.log(limes.length)
  }
}

const limes = [
  'small',
  'large',
  'large',
  'medium',
  'small',
  'large',
  'large',
  'medium',
];

limesToCut(42, limes)

// while (soma <= wedgesNeeded) {
//   let limesLength = limes.length
//   switch (limes){
//   case 'small':
//     limes.shift()
//     soma += 6
//     break;
//   case 'medium':
//     limes.shift()
//     soma += 8
//     break;
//   case 'large':
//     limes.shift()
//     soma += 10
//     break;
//   }
//   return limesLength
// }

// return 