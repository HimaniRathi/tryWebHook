require 'sinatra'
require 'json'


post '/payload' do
  push = JSON.parse(request.body.read)
  puts "I got some JSON that i am trying to print: #{push.inspect}"
end
