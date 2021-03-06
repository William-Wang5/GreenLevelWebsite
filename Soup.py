import requests
from bs4 import BeautifulSoup
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

list = []

page = requests.get(
    "https://www.wcpss.net/Page/35447")
soup = BeautifulSoup(page.content, 'html.parser')
soup = soup.find_all(class_="sw-calendar-block-title")

for link in soup:
    date = str(link).split(">")
    event = date[-3]
    event = event.split("<")
    list.append([event[0]])
if len(list) <= 5:
    for i in range(len(list), 7):
        list.append([])
print(list)


options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options)
driver.get("https://www.wakecountyathletics.com/greenlevel")
String = driver.page_source
String = String.split("table")
String = String[4]
String = String.split("data-week-view-date")


for i in range(1, 6):
    if "noEntry" in String[i]:
        pass
    else:
        tempString = String[i].split(">")
        tempString = tempString[4].split("<")
        list[i - 1].append(tempString[0])

print(list)
jsPart1 = """

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
    document.getElementsByClassName("day-date")[x].innerText = months[month] + " " + (parseInt(date.getDate() + x));

    if (schoolDay < 6) {
      schoolDay += 1;
    } else {
      schoolDay = 0;
    }
  }
}
change();

"""
with open(r"C:\Users\willi\Desktop\Visual Studio\script.js", "w+") as file:
    file.write("\n" + "list = " + str(list) + "\n" + jsPart1)
