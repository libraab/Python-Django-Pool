#curl = upload the page
#-s = silently
# grep all the line where the word moved is
# on x grep till >moved
# on y grep from =
# last line = trim z from (1) to (len of z -2)
x=$(curl -s $1|grep "moved")
y=${x%>moved*}
z=${y##*=}
echo ${z:1:${#z}-2}

