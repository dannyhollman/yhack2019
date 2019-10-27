#!/usr/bin/ruby

lines = []
File.open("jetblue_twitter.json", "r").each_line do
	|l|
	lines << l.gsub(/\\\\\\\\/, "\\").gsub(/\\u..../, "").gsub(/http:\\\/\\\/.*?\\\//, "").gsub("#","").gsub("@","").gsub("\\", "the").gsub("&amp;", "and")
end

File.open("jetblue_twitter.json", "w") do
	|f2|
	lines.each do
		|l|
		f2.puts(l)
	end
end
