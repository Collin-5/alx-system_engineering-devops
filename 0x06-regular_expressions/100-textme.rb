#!/usr/bin/env ruby
# match sender,receiver,flags
puts ARGV[0].scan(/\[(?:from:|to:|flags:)(.*?)\]/).join(",")
