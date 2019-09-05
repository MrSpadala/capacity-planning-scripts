
"""MVA.py: Input the service time of queues in series and N, which is for how many requests 
in the system you want to calculate the results. It then outputs the mean response time,
mean throughput and how the requests are "spread" inside the different queues, for each
number of requests from 1 to N"""

__author__      = "Pietro Spadaccino"




def MVA(D_queues, N):

	n_prev = [0] * len(D_queues)    #n_prev[i] = users in queue i at previous MVA step

	for i in range(1, N+1):
		# Use MVA equations
		R = [D_queues[j]*(1+n_prev[j]) for j in range(len(D_queues))]
		R_tot = sum(R)
		X = i/R_tot
		n_prev = [X*r for r in R]

		status = f""">>> N = {i}
	R({i}) = {R_tot/1000:.3f} s
	X({i}) = {1000*X:.2f} requests/s
	n in queues: {[f'{n:.2f}' for n in n_prev]}
	- - - - - - - - - - - - - - -
	"""
		print(status)




if __name__ == '__main__':
	n_queues = int(input("Number of queues in series: "))
	D_queues = []
	for i in range(n_queues):
		D = input(f"Insert service time (D) of queue {i} (in ms): ")
		D_queues.append(int(D))

	N = int(input("Input N (calculate MVA from 1 to N incoming requests ): "))

	MVA(D_queues, N)











def print_ciciani():
	print("""
sssyyyyyyyyssssssssssssssssssssssssssssssssyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyhhhhhhhhhhhhhhhhdddddddddddmmmmm
ssshyyyhhyhhhhhhhhhhhhyhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhddddddddddddddddddddddmmmmmmmmmmmmmmmmNNm
ssshyyyhddddddddddddddddddddddddhhhhhhhhhhhhhhhhddddddddddddddddddddddddhhdddddddddddddddddmmmmmmmmmmmmmmmmNNm
ssshyyyhddddddddddddddddddddddddddddddhhhdddhyyyyhhhhhhhhhhhhhhhhhdddddhyydddddddddddddddddmmmmmmmmmmmmmmmmNNm
ssshyyyhdddddddddddddddddmmmmmNNNmNmmmdddddhhyysossyhhhhhhhhhhhhhhhhdhdhyyhddddddddddddddddddddmmmmmmmmmmmmmNm
ssshyyyhdhdddddddddhddmmmmmmmNNNNNmdmmmdddmdhhhyyosssyhhhhhhhhhhhhhhhhdhyyhdddddddddddddddddddddddmmmmmmmmmmNm
soshyyyhdhddddddddddmmmmNNNNNNNNNNNmmmNdhmddhyyyysooo+syhhhhhhhhhhhhhhhhyyhdddddddddddddddddddddddddmmmmmmmmNd
soshyyyhdhhddddhhddmmmNNNNNNNNNNNNmdddddddddhysshyso+++syyyyyhhhhhhhhhhhyyhdhhddddddddddddddddddddddddmmmmmmmd
ssshyyyhhhhddddhddmmmNNNNNNNNNMMNNmddhdmdhhdysoohyso+///syyyyyyyyhhhhhhhsyhdhhhdddddddddddddddddddddddddmmmmmd
ssshyyyhhhhhhhdddmmmNNNMMMMMMMNNNNdddhdhhhhsoooshs+/+//:/yyyyyyyyyyyhhhhsshhhhhhhhhhdddddddddddddddddddddmmmmd
ssshyyyhhhhhhddmmmmmNNMMNNNMMNNmNmddhhhhyyyo+sssy+/:://:-syyyyyyyyyyyhhysshhhhhhhhhhhddddddddddddddddddddmmmmd
sssyyyyhhhhhhdmmmmmNNNNNNNNNNNmmmmdhhhhysso+syoo+/:----..ossssyyyyyyyyhysshhhhhhhhhhhdddddddddddddddddddddmmmd
sssyyyyhhhhhhmNmmmNNmmNNNmmmmmmmdddhhhdhyyo++++//:-----..+sssssyyyyyyyyysshhhhhhhhhhhhhdddddddddddddddddddmmmd
sssyssshhhhhdmmmmmmddmNNmmmmddmddhdddddhyso//:--/++osso+-osssssssyyyyyyysshhhhhhhhhhhhhhddddddddddddddddddmmmd
sssyssshhhhhdmmmmNdddNmmmmddddddddmmmmmddyso//:-/++ooo/::osssssssssyyyyysshhhhhhhhhhhhhhhdddddddddddddddddmmmd
sosyysshhhhhdmmmmmmdmNmmmmdddddddmNNNmdhssoo++/--+oos+:--oosssssssssyyyysshhyhhhhhhhhhhhhhhdddddddddddddddmmmd
sssyssshhhhhdmmmmmmdmNNmNmmddddddmmmmhyo///odhy+:oyhd/-/-/oosssssssssyyysshyyyhhhhhhhhhhhhhdddddddddddddddmmmd
sssyysshhhhhdmmNmmmmdNNNNmmdddddddddddmh/+ydNmdhs/ooo/-../ooosssssssssyysshyyyhhhhhhhhhhhhhhdddddddddddddddmmd
ossyssshhhhhhddNNmmmmmNNNmmdddddddmmmmdhsshmNmmdds/::---./oooossssssssyysshyyyyyhhhhhhhhhhhhdddddddddddddddmmd
sssyssshhhhhhddmNmmmNdNNNNNmdddddmmddhyyhdmmmmmddho:----.:oooooossssssyysshyyyyyhhhyhhhhhhhhdddddddddddddddmmd
sssyssshhhhhhhdmmmmmNmmNNNNmddddddddhyhdmmmmmmddddy/.--..-ooooososssssyysshyyyyyhhyyhhhhhhhhdddddddddddddddmmd
sssyssshhhhhhddmNNmmNmNNNNNmdddddddddhddddmmmdddddy/-:-.`-oooooossssssyysshyyyyyhhhyhhhhhhhhdddddddddddddddmmd
sssyssshhhhhhhdmNNmmmmmmmNmmddddddddddhhyyydmddNNho/-::-..+ooooossssssyysshyyyyyyhhyhhhhhhhhdddddddddddddddmmd
sssyssshhhhhhhhddmmmdddmmmmmmmdddmmdddhysoydmmNmmsso+/+/-./osooossssssyysshyyyyyhhyyhhhhhhhhdddddddddddddddmmd
sssyssshhhhhhhhhhdmNNmdmmmdmdddmmmmdddhyyhmmmmmmhsyo/+o+-./ossssssssssyysshyyyyyyhyhhhhhhhhhdddddddddddddddmmd
sssyssshhhhhhhhhhhdNNMNmmmddmmddmmmmddyydmmNmmddyo+/::s/-.+sssssssssssyysshyyyyyyhhhhhhhhhhhdddddddddddddddmmd
sssyssshhhhhhhhhhhhdNMMMMmddmmdddddddhyydmNmmmddyo+:-.+/::ssssssssssssyysshyyyyyhhhhhhhhhhhddddddddddddddddmmd
sssyssshhhhhhhhhhhhhmNNNNmmddddddddddhhydmmmddhyys+/--::-ossssssssssssyysshyyyyyhhhhhhhhhhhddddddddddddddddmmd
sssyssshhhhhhhhhhhhhhhdhhdddddddhddddddddmdddhysso+:---:+sssssssssssssyysshyyyyhhhhhhhhhhhhddddddddddddddddmmd
sssyssshhhhhhhhhhhhhhdhyyhddddddhhhddmmmmmdddhyso+/:-.:ossssssssssssyyyysshyyyhhhhhhhhhhhhhddddddddddddddddmmd
sssyssshhhhhhhhhhhyhmmdhyyhhdmddddhdddddddddhysoo+/:-.+ssysssssssssyyyyysshyyhhhhhhhhhhhhhhddddddddddddddddmmd
sssyssshhhhhhhhhhyyhdmdmdhyyyhddddhhhdddddhyso++/::.-osyyyyyyyyyyyyyyyhysshyyhhhhhhhhhhhhddddddddddddddddddmmd
sssyssshhhhhhhhhhhhhhhhdmmdhyyyhddddhhhhhhyso::-..:/.-://+ossyyyyyyyyyhysshhhhhhhhhhhhhhhddddddddddddddddddmmd
sssyssyhhhhhhhhhhhhhhdddhdmmhyyyhhddhhyyysso/-.`.-s+..-.-...-:/+osyyyyhysshhhhhhhhhhhhhhhddddddddddddddddddmmd
sssyssyhhhhhhyyyyyyhyyyhdhhdmdhyyyyyyssysso+:-...sy+.```.::-...-::/oyyhysshhhhhhhhhhhhhhhddddddddddddddddddmmd
sssyysyhhhyyyyyssyyyyssssyddhdmdhyysso/:::----..+doyy+.``.-/:-...::--/sysshhhhhhhhhhhhhhdddddddddddddddddddmmd
sssyysyhyyssoooossssssssoooshhdmdddhysso/:----/+hosyhNs.```.://:-..--.-:oshhhhhhhhhhhhhhdddddddddddddddddddmmd
sssyyyyyyssooo+++//+ooosooo+/+ydmhyhmdhssoo+/yhyyyssoo-:.````:///:-.-...-+hhhhhhhhhhhhdddddddddddddddddddddmmd
sssyyyyyysoo+///::---:/++o+oo///sddhyyhdhsooydddhhyso+`./.````-//+/:--...`-+yhhhhhhhhdddddddddddddddddddddmmmd
ssyyyyyyyyyso+:--:----::::/++o+/:/sdhysssssooNNNNmdyso:``/`````./+++/:...```-/yhhhhhhdddddddddddddddddddddmmmd
syyyyyyyyyssosso/:---.-::---:/+++/-:yyhys+/--shmNNNmys+``.:`````.:+++/:...`.`::+hhhhddddddddddddddddddddddmmmd
yyyyyyyyysso+//+ss+:---.-::--.-/++/--+osyss+/:--:/osoyy.``.:`````.:+o+/-`.....+--yhhddddddddddddddddddddddmmmd
yyyyyyyyyys+sso+/+oo+::--.-::---:+++:.///sssso/:----...````.:`````./oo+/.`.```+/.-hhddddddddddddddddddddddmmmd
yyyyhhhhyyyo++oyys+++o+::--.-----:/++:.::-/+ssso/----.``````.:``````/oo+-`--``+/-`+hddddddddddddddddddddddmmmd
yyhhhhhhdhhhyyo+/osoo//++:---...-://+/:.-/..:+oso+:---.``````.:``````/o+/`-:..+/-`.yddddddddddddddddddddddmmmd
yyyhhhhhhhhdddhys+/+yyo//++:--...--/+++:.-:...-/os+:...```````.:.`````/o+.:/-.::.``ohdddddddddddddddddddddmmmd
yyhhyhhhhhhhhhdddhyo/+ss+-:++:-....-:/++/-./....-/o+:..````` `..:.`````/o/./:`:-.```:yddddddddddddddddddddmmmd
yyyhhhhyyyyhhhyyyhhhyo+/oo:-/+:-..`..-/++/-.:.....:++:.```````-.`:.`````:+:-/.:-.``  .ydddddddddddddddddddmmmd
yyyyhhhhdhyssssssoosyyys/:++--:/-..```.:/+/-.:-.-..-//-.``````+o/:+.`````-/-:-:-..` ``-yddddddddddddddddddmmmd
yyyyyyyyyyhhyso++++//+oss+/:+/--:-..```.-///:-:-:o-..-:-```````...-//-` ``.-.-://-```.`:sdddddddddddddddddmmmd
yyhhyyyhhyyysssss++//:://++/:++:-:-..```.-://:::++o/.`--.```````..``:/-``````./o+-``..``.:ydddddddddddddddmmmd
yyyhhyyhhhhhyysoo+++//:::::::-/o/::-...``..-://:::-/o-`..````````..``-+.``````+o/.`..:-```.oddddddddddddddmmmd
yyyhhyyyhhhhhhhhyso+/:::---::--/so/:-.-.```.-:///-:-/o.`..```````...``/+` ````oo/.`.-+:` `..sdddddddddddddmmmd
yyyyhhhyyhhhhhhhhhhyso+:-...-::-/so+/-.--.``.-://:.:-o:.``````````..```:`  ```/+:`.-:o:``-.`./shddddddddddmmmd
yyyyyhhhhyyhhhhddhhhhhyyo+:...--:/yo+/-.--.``.--::-./+/-.``````````.``````  ` :/-`-:+o-`--.`` `:sdddddddddmmmd
yyyyyhhhhhyyhhhhhhddhhhhhyyo/:..--oho+/-.:-.`..--:---++-.`````````````````   `-/.-+os+..--::.`.``/hdddddddmmmd
yyyyyyhhhhhyyhhhyyyyhhhhhhhhyso/---sho+/-.--.......---...````````.````````    --.oo/o+--:/:/o/.`  .sddddddmmmd
hyyyyyyhhhhhyyhhhysoosyhhyyyyyyyo+::+o++/-.-....``...--...`````````````````   .-++/:oo++:--://o/-` -ydddddmmmd
hyyyyyyyhhhhhyyyhhysooosyyso++ossso+:--:/:-.-`.:-.`.``.-.`````````.````````  `:+o/+ss+:-:/:-..++/:-.-ohdddmmmd
hhhyyyyyyhhhhhhyhhysoo++ossys+/::/+++/-..::-.-.-/-.`.``.-.`.``````..````.`.```+++sys+:-/+:----::--..``-ohdmmmd
hhhhyyyyyyhhhhhhhyhyso++++oooso+-.-::::-..-:--:-:/:.````-:``.``````..```...``-++yyss+oo+/:/:--..````````-sdmmd
hhhhhyyyyyyhhhhhhhyhhyo++++ooooso/-..----.`.:--+::::.````-.`.``````..```....`+sydssoss+//::-.--..`` ``   `+dmd
hhhhhhyyyyyyhhhhhhhhhhyo+/++ooooooo/-......`.--:o/--:-.``.....``.`.--.......-+oso+///-...`....`````       `+dd
yhhhhhhyyyyyyhhhhhhhhhhys+///++ooooo++:-...```.-:o+:/o/``..--/.-/:-::-...-/+ooo+/:-.````````````        `` `/h
hhhhhhhhyyhyyhhhhhhhhhhhys+/////+++o+++/-.....`..+so+ys/-::::/::::://:.......-/+oo+/-.``` ``            ```  +
hhhhhhhhhhhhhhhhhhhhhhhhhys+///////+++++/-.`.`...:so+/////++++++++///ss/...``..-:/+++/-```               `.` -
hhdhhhhhhhhhhhhhhhhhhhhhhhhso+///::///+++/-..```.`:+:////++ooo+++o+/::ohy/.```...-/+/::.`                 `.`:
hhhhhhhhhhhhhhhhhhhhhhhhhhhhyso++/::-::/++/:-..```.//++++oooooo+o++/::/sddo`````.-:+o+/-```` ```           ``+
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhysoo+++/:---:::/:-..``-/++ooosssssooooo+//sddd/`````.-:/o+/.``````            `-h
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhysoooo++/::--------....:ooosssssssoooo++oymmmm/```....-///-.``             ``/hd
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhysoooo++/:::-----..````:/ossssssosssoooshdmNNd``.---....``````       `    .ymmd
hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhyssoooo+:----:----..`::..+sssssooossyhdmNNNm+..-:////:-----::--...`````-+hmmmd
hhhhhhhhhhhddhhhhhhhhhhhhhhhhhhhhhssssss+:...------:/:.```.-:/+oohhdmdddddhsooooossssooo++//:--.......oddmmNmd
mhhhhhhhhhddmddhhhhhhhhhhhhhhhhhhhhyssysso:.`..-:++/-..`....``---s+/o+syo:/oyhhyyysssoo++////:::-..`-yddmmmNmd
Nhhhhhhhhhddddddhhhhhhhhhhhhhhhhhhhhysyyyys+----::-....``...`--`.:.-:.:+/..--:/sy+oydyso/::--....`.+ddmmmmmNmm
Mhhhhhdhhhhddddddhhhhhhhhhhhhhhhhhhhhyyyyhyys+//:-......--../:`...`--``--.`...-//.-:+ydhys+/::-::odmmmmmmmmNmm
Mhyhhhhhhhhhhhhhhdmdhhhhhhhhhhhhhhhhhhhyyyyys+::-.....-:-.-:-`...``-.``..`.```-:-`-/sddddddddddddmmmmmmmmmmNmm
""")
