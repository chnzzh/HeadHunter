#!/bin/bash
echo "Copying headhunter psudo binary"
cp bin/headhunter /usr/bin
chmod +x /usr/bin/headhunter
echo "Setting execute permissions"
cp -r ../HeadHunter /usr/share/
echo "Moving headhunter source tree to /usr/share/HeadHunter"

