#!/usr/bin/env ruby
# Match "hbt....n,
puts ARGV[0].scan(/hbt{2,5}n/).join
