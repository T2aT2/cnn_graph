y = open('Y','r');
num_vid = open('num_vid','w');
cn = 1;
i = 0;
for line in y:
	li = line.split();
	if i==0:
		pre = li[0];
		i+=1;
		continue;
	if pre!=li[0]:
		num_vid.write(str(cn)+'\n');
		cn = 1;
	else:
		cn+=1;
	pre = li[0];
num_vid.write(str(cn));
