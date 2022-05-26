
list = [['Community Use Rental'], ['Memorial Day - No School'], ['Exam Review Day'], ['Community Use Rental'], ['Semester Two Exam Week'], [], []]


const times = [
  "7.25",
  "8.45",
  "8.50",
  "9.15",
  "9.20",
  "10.40",
  "11.25",
  "12.10",
  "12.50",
  "14.18",
];
const periods = [
  "Until 1st period",
  "Until gator time",
  "Passing period",
  "Until 2nd period",
  "Passing period",
  "Until 3rd period",
  "Until end of Lunch A",
  "Until end of Lunch B",
  "Until 4th period",
  "Until end of school",
];
const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

function currentTime() {
  let date = new Date();
  let day = date.getDay();
  let hh = date.getHours();
  let mm = date.getMinutes();
  let ss = date.getSeconds();
  document.getElementsByClassName("date-text")[0].innerText = days[0] + ", " + months[date.getMonth()] + " " + date.getDate();
  let time = parseFloat(mm / 100) + parseInt(hh);
  if (day == 6) {
    let time = (8 - day) + " day(s) until school"
    document.getElementsByClassName("circle-text")[0].innerText = time;
    let t = setTimeout(function() {
      currentTime()
    }, 1000);
  } else if (day == 0 || time > 14.18) {
    hh = Math.floor((1885 - (mm + hh * 60)) / 60);
    mm = (Math.floor((1885 - (mm + hh * 60)) % 60) > 0) ? Math.floor((1885 - (mm + hh * 60)) % 60 - 1) : Math.floor((1885 - (mm + hh * 60)) % 60);
    ss = 60 - ss - 1;
    hh = (hh < 10) ? "0" + hh : hh;
    mm = (mm < 10) ? "0" + mm : mm;
    ss = (ss < 10) ? "0" + ss : ss;
    document.getElementsByClassName("circle-time")[0].innerText = hh + ":" + mm + ":" + ss;
    document.getElementsByClassName("circle-text")[0].innerText = " Until first Period";
    let t = setTimeout(function() {
      currentTime()
    }, 1000);
  } else {
    for (let i = 0; i < times.length; i++) {
      if (parseFloat(times[i]) > time) {
        let splitTime = times[i].split(".");
        let newtime = parseFloat(splitTime[0]) * 60;
        newtime += parseFloat(splitTime[1])
        hh = Math.floor((newtime - (mm + hh * 60)) / 60);
        mm = (Math.floor((newtime - (mm + hh * 60)) % 60) > 0) ? Math.floor((newtime - (mm + hh * 60)) % 60 - 1) : Math.floor((newtime - (mm + hh * 60)) % 60);
        ss = 60 - ss - 1;
        hh = (hh < 10) ? "0" + hh : hh;
        mm = (mm < 10) ? "0" + mm : mm;
        ss = (ss < 10) ? "0" + ss : ss;
        document.getElementsByClassName("circle-time")[0].innerText = hh + ":" + mm + ":" + ss + " ";
        document.getElementsByClassName("circle-text")[0].innerText = periods[i];
        break;
      }
    }
    let t = setTimeout(function() {
      currentTime()
    }, 1000);
  }
}
currentTime();

function change() {
  let date = new Date();
  let day = date.getDay();
  let schoolDay = day;
  let month = date.getMonth()
  let monthDate = date.getDate()
  for (var x = 0; x < 7; x++) {
    if (list[x] != "") {
      for (var b = 0; b < list[x].length; b++) {
        var board = document.createElement('div');
        if (list[x].length > 1){
        if (x % 2 == 0){
            board.className = (b % 2 == 0) ? board.className = "event1" : board.className = "event2";
        } else{
        board.className = (b % 2 == 0) ? board.className = "event2" : board.className = "event1";
        }
        } else{
        board.className = (x % 2 == 0) ? board.className = "event1" : board.className = "event2";
        }
        board.innerText = list[x][b];
        board.classList.add("the-event")
        document.getElementsByClassName("amazing-events")[x].appendChild(board);
      }
    }
    else{
      var board = document.createElement('div');
      board.className = (x % 2 == 0) ? board.className = "event1" : board.className = "event2";
      board.innerText = "Nothing for today!";
      board.classList.add("the-event")
      document.getElementsByClassName("amazing-events")[x].appendChild(board);
    }
    document.getElementsByClassName("day-header")[x].innerText = days[schoolDay];
    let dayDate = 0;
    let doop = false;
    if ((month) % 2 == 0){
      console.log(month);
      if ((date.getDate() + x) > 31){
        console.log(date.getDate() + x);
      dayDate = (x + 1) - x;
      doop = true;
      } else{
        dayDate = date.getDate() + x;
      }
    }
    if (doop){
    document.getElementsByClassName("day-date")[x].innerText = months[month + 1] + " " + (parseInt(dayDate));
    }else{
      document.getElementsByClassName("day-date")[x].innerText = months[month] + " " + (parseInt(dayDate));

    }
    if (schoolDay < 6) {
      
      schoolDay += 1;
    } else {
      schoolDay = 0;
    }
  }
}
change();

