# Version: MPL 1.1/LGPL 2.1
#
# This file is part of the LibreOffice project.
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# Contributor(s):
# Rasmus P J <wasmus@zom.bi>
#
# Alternatively, the contents of this file may be used under the terms of
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL or the LGPL.
#
#

from enum import Enum

class Request(Enum):
    # choose a file to play
    PLAY_FILE       = 1
    # pause current file
    PAUSE           = 2
    # remove a file from playlist
    REMOVE_FILE     = 3
    # add file to playlist
    ADD_FILE        = 4
    # change order of files (item.pop(i), item.insert(j))
    ORDER           = 5
    # play/ unpause current file
    PLAY            = 6
    # move file from files list to playlist
    QUEUE_FILE      = 7

