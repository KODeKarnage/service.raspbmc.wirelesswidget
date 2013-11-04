# declare file encoding
# -*- coding: utf-8 -*-

#  Copyright (C) 2013 KodeKarnage
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html

#FOUND THE FUNCS HERE
#http://talk.maemo.org/showthread.php?t=55436

import xbmcgui
import xbmcaddon
import xbmc
import os

__script_id__ = "service.raspbmc.wirelesswidget"
__addon__ = xbmcaddon.Addon(id=__script_id__)
__scriptPath__ = __addon__.getAddonInfo('path')
__setting__ = __addon__.getSetting

freq = int(__setting__('freq'))
xax = int(__setting__('xax'))
yax = int(__setting__('yax'))

qual = __setting__('qual')
rssi = __setting__('rssi')
noise = __setting__('noise')
cputemp = __setting__('cputemp')
gputemp = __setting__('gputemp')

sett = []
if qual == 'true':
	sett.append('qual')


def log(vname, message):
	#if settings['debug']:
	xbmc.log(msg=vname + " -- " + str(message))

def funcCpuTemp():
	ga = os.popen('cat /sys/class/thermal/thermal_zone0/temp').read()
	go = float(ga)/1000
	return  '%.1f°C' % go


def funcGpuTemp():
	ga = os.popen('/opt/vc/bin/vcgencmd measure_temp').read()
	go = str(ga).replace('temp=','').replace("'C",'')
	return go.strip() + '°C'	


def funcWifiLinkQ():
    # "** Start Function - Wireless Link Quality **"
    ga = os.popen('cat /proc/net/wireless | awk \'/0/ {print $3}\' | awk -F. \'/./ {print $1" %"}\'').read()
    return ga.strip()

def funcWifiRSSI():
    # "** Start Function - Wireless RSSI **"
    ga = os.popen('cat /proc/net/wireless | awk \'/0/ {print $4" dBm"}\'').read()
    return ga.strip()

def funcWifiNoise():
    # "** Start Function - Wireless Noise **"
    ga = os.popen('cat /proc/net/wireless | awk \'/0/ {print $5}\' | awk -F. \'/./ {print $1" dBm"}\'').read()
    return ga.strip()


def Main():
	window = xbmcgui.Window(10000)
	count = 0
	for x in sett:
		exec 'wwidgl%s = xbmcgui.ControlLabel(xax, yax+%i, 350, 50, "Scanning...")' % (count,count*25)
		exec 'window.addControl(wwidgl%s)' % count
		count += 1

	while not xbmc.abortRequested:
		xbmc.sleep(1000*freq)
		count = 0
		for x in sett:
			exec 'wwidgl%s.setLabel("%s" + str(%s))' % (count,x[0],x[1])
			count += 1
	count = 0 
	for x in sett:
		exec 'window.removeControls([wwidgl%s])' % count
		count += 1

sett = []

if qual == 'true':
	sett.append(('Wireless Quality: ','funcWifiLinkQ()'))
if rssi == 'true':
	sett.append(('Wireless RSSI: ','funcWifiRSSI()'))
if noise == 'true':
	sett.append(('Wireless Noise: ','funcWifiNoise()'))
if cputemp == 'true':
	sett.append(('CPU Temp: ','funcCpuTemp()'))
if gputemp == 'true':
	sett.append(('GPU Temp: ','funcGpuTemp()'))


if __name__ == "__main__":
	Main()

