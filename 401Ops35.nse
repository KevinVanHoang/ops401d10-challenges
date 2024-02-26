-- SimpleInfo.nse
-- Script Name:                  Simple Information Gathering Script
-- Author:                       Your Name
-- Date of latest revision:      Your Date
-- Purpose:                      Gathers IP address and port status for the target

description = [[
Gathers basic information about a target host.
]]

author = "Your Name"
license = "Same as Nmap--See https://nmap.org/book/man-legal.html"
categories = {"default", "safe"}

portrule = function(host, port)
    -- The portrule should return true if the script should run on the given host/port pair.
    -- For simplicity, we will just return true to run on all hosts and ports provided to Nmap.
    return true
end

action = function(host, port)
    -- The action function performs the actual work of the script and returns the result as a string.
    local host_ip = host.ip or "n/a"
    local port_status = (port.state == "open") and "Open" or "Closed"

    -- Format the output
    local output = string.format("Host IP: %s\nPort %s: %s\n", host_ip, port.number, port_status)

    return output
end
