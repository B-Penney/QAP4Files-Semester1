const MotelCustomer = {
  name: "",
  birthDate: "",
  roomPref: [],
  pmtMethod: "",
  mailAdd: {
      street: "",
      city: "",
      prov: "",
      postCode: ""
  },
  phoneNum: "",
  checkInDate: "",
  checkOutDate: "",

  // Method to calculate the age of the customer
  calculateAge: function() {
      const birthYear = new Date(this.birthDate).getFullYear();
      const currYear = new Date().getFullYear();
      return currYear - birthYear;
  },

  // Method to calculate the duration of stay in days
  calculateStayDuration: function() {
      const checkIn = new Date(this.checkInDate);
      const checkOut = new Date(this.checkOutDate);
      const timeDiff = Math.abs(checkOut - checkIn);
      return Math.ceil(timeDiff / (1000 * 60 * 60 * 24));
  },

  // Method to generate a description of the customer
  generateDescription: function() {
      return `<p>Name: ${this.name}
      Age: ${this.calculateAge()}
      Room Preferences: ${this.roomPref.join(', ')}
      Payment Method: ${this.pmtMethod}
      Mailing Address: ${this.mailAdd.street}, ${this.mailAdd.city}, ${this.mailAdd.prov} ${this.mailAdd.postCode}
      Phone Number: ${this.phoneNum}
      Check-In Date: ${this.checkInDate}
      Check-Out Date: ${this.checkOutDate}
      Stay Duration: ${this.calculateStayDuration()} days`;
  }
};

// Set customer attributes
MotelCustomer.name = "Beth-Ann Penney-Rideout";
MotelCustomer.birthDate = "1995-09-21";
MotelCustomer.roomPref = ["Non-smoking", "King-size bed", "Bathroom", "Kitchen", "Balcony", "Complimentary breakfast"];
MotelCustomer.pmtMethod = "Credit Card";
MotelCustomer.mailAdd.street = "123 Main St";
MotelCustomer.mailAdd.city = "GFW";
MotelCustomer.mailAdd.prov = "NL";
MotelCustomer.mailAdd.postCode = "123 456";
MotelCustomer.phoneNum = "999-999-9999";
MotelCustomer.checkInDate = "2024-03-24";
MotelCustomer.checkOutDate = "2024-03-28";

// Display customer description as HTML paragraph
const customerDescriptionHTML = MotelCustomer.generateDescription();

console.log(customerDescriptionHTML);

// Room preference sentence
let roomPreferenceSentence = `This Motel offers ${MotelCustomer.roomPref[0]} with a ${MotelCustomer.roomPref[1]}, and a beautiful ${MotelCustomer.roomPref[2]}, and ${MotelCustomer.roomPref[3]} with a ${MotelCustomer.roomPref[4]} with an absolutely stunning view! Complete with ${MotelCustomer.roomPref[5]}, We hope you thoroughly enjoy your stay!`;

console.log(roomPreferenceSentence); //sends to console