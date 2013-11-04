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

def log(vname, message):
	#if settings['debug']:
	xbmc.log(msg=vname + " -- " + str(message))


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
	wwidgl1 = xbmcgui.ControlLabel(xax, yax, 350, 50, 'Scanning')
	wwidgl2 = xbmcgui.ControlLabel(xax, yax+25, 350, 50, 'Scanning')
	wwidgl3 = xbmcgui.ControlLabel(xax, yax+50, 350, 50, 'Scanning')
	window.addControl(wwidgl1)
	window.addControl(wwidgl2)
	window.addControl(wwidgl3)

	while not xbmc.abortRequested:
		xbmc.sleep(1000*freq)
		wwidgl1.setLabel('Quality: ' + str(funcWifiLinkQ()))
		wwidgl2.setLabel('RSSI: ' + str(funcWifiRSSI()))
		wwidgl3.setLabel('Noise: ' + str(funcWifiNoise()))

	window.removeControls([wwidgl1,wwidgl2,wwidgl3])

if __name__ == "__main__":
	Main()

