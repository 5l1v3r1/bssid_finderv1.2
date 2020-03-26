#!/bin/python3
from tkinter import messagebox
from tkinter import *
import folium
import urllib.request
import os
def create_window():
 global window,text_field
 window=Tk()
 window.title("MAC FINDER V1.2 by Zert")
 window.geometry('400x150')
 window.config(bg='black') 
 lbl = Label(window, text="Enter MAC", font=("Arial Bold Italic", 10),bg='black',fg='white')
 lbl.place(x=173,y=1)
 text_field=Entry(window,width=25,bg='grey',fg='white')
 text_field.place(x=100,y=20)
 btn = Button(window, text="FIND",command=get_mac,bg='black',fg='white')
 btn.place(x=175,y=70)
 window.resizable(False,False)
 window.mainloop()
def main():
 create_window()
 #mac=get_mac()
 #print(mac)
 #find(mac)
def find(mac):
 link="http://mobile.maps.yandex.net/cellid_location/?clid=1866854&lac=-1&cellid=-1&operatorid=null&countrycode=null&signalstrength=-1&wifinetworks="+mac+":-65&app=ymetro"
 try:
  page = urllib.request.urlopen(link)
  out=str(page.read())
 except:
  print("ERROR or Not found")
  exit(0)
 location=clean_string(out)
 #print("Location found:{}".format(location))
 messagebox.showinfo('Location found:','Coordinates:{}'.format(location))
 choice=messagebox.askyesno('Save map', 'Save map with this location?')
 if choice == True:
  create_coordinates(location)
def create_map(lan,lon):
 #map = folium.Map(location=[lan,lon], zoom_start = 6, tiles = "Mapbox bright")
 my_map2 = folium.Map(location = [lan,lon],zoom_start = 12)
 folium.Marker(location=[lan,lon], popup = "Found Location", icon=folium.Icon(color = 'green')).add_to(my_map2)
 my_map2.save("map"+str(lan)+':'+str(lon)+'.html')
def create_coordinates(location):
 global lan,lon 
 lan=float(location[location.find('"')+1:location.find('=')-33])
 lon=float(location[location.find('gitude')+8:-2])
 create_map(lan,lon)
def get_mac():
 if text_field.get() != "":
  find(text_field.get().replace(':','').upper())
 else:
  messagebox.showerror('Error', 'Field is empty!')
def clean_string(text):
 return text[text.find('la'):text.find('nl')].replace("b'","").strip()
main()
