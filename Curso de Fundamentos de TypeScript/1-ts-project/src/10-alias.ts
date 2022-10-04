(()=>{
  type UserID = string | number | boolean;

  let userId: UserID;

  // Literal types
  type Sizes = 'S'|'M'|'XL'|'L';
  let shirtSize: Sizes;
  shirtSize = 'M';
  function greeting(userId: UserID, size:Sizes) {
    if (typeof userId === 'string') {
      console.log(`string`)
    }
  }

  greeting(1111, 'M');



})();
