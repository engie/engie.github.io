jekyll --server &
echo $! > pids/jekyll.pid
sass --watch _sass:css &
echo $! > pids/sass.pid


