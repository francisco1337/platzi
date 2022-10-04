(()=>{
  // let myNumber: number = undefined;
  // let myString: string = null;
  let myNull: null = null;
  let myundefined: undefined = undefined;

  function hi(name: string | null) {
    let hello = 'hola';
    if (name) {
      hello +='name';
    } else {
      hello +='nobody';
    }
    console.log(hello)
  }

  hi("francisco");
  hi(null);

})();
