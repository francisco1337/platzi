(()=>{
  let userId: number|string;

  function greeting(myText: string|number) {
    if (typeof myText === 'string') {
      myText.replace("a","b");
    } else {
      myText.toFixed(2);
    }
  }
  greeting("as");
  greeting(12.12121);
})();
