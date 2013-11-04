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

import xbmcgui
import xbmcaddon
import xbmc

import sys
sys.stdout = open('C:\\Temp\\test.txt', 'w')

__script_id__ = "service.raspbmc.wirelesswidget"
__addon__ = xbmcaddon.Addon(id=__script_id__)
__scriptPath__ = __addon__.getAddonInfo('path')
__setting__ = __addon__.getSetting

def Main():
	__addon__.openSettings()

if __name__ == "__main__":
	Main()

