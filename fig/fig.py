import matplotlib.pyplot as plt

x = [2500, 3000, 3500, 4000, 4500, 5000]
ems3 = [537, 759, 957, 1098, 1173, 1249]
bas3 = [841, 1184, 1416, 1522, 1610, 1674]
ems2 = [986, 1266, 1498, 1664, 1791, 1818]
bas2 = [1143, 1507, 1796, 2018, 2190, 2297]
ems1 = [1233, 1607, 1895, 2146, 2333, 2449]
bas1 = [1363, 1757, 2067, 2337, 2535, 2686]

plt.figure(1)
plt.xlabel('Network Size')
plt.ylabel('Time')
plt.plot(x, ems3, '-ks')
plt.plot(x, bas3, '-k^')
plt.plot(x, ems2, '-ks')
plt.plot(x, bas2, '-k^')
plt.plot(x, ems1, '-ks')
plt.plot(x, bas1, '-k^')
plt.annotate('i=3', xy=(4600, 1200), xytext=(4800, 1400), arrowprops=dict(facecolor='black'))
plt.annotate('i=2', xy=(4800, 1600), xytext=(4800, 2000))
plt.annotate('i=1', xy=(4800, 2400), xytext=(4800, 2500))
plt.grid()
plt.axis([2500, 5000, 500, 2800])
plt.savefig('embas.png')
# plt.show()
plt.close(1)

bkems3 = [3501, 4055, 4430, 4780, 4945, 5052]
bksts3 = [5390, 5984, 6474, 6909, 7184, 7379]
bkems2 = [5730, 6302, 6781, 7209, 7528, 7753]
bksts2 = [7097, 7797, 8411, 8929, 9368, 9668]
bkems1 = [7436, 8128, 8765, 9237, 9660, 10014]
bksts1 = [8209, 9032, 9733, 10319, 10836, 11225]

plt.figure(2)
plt.xlabel('Network Size')
plt.ylabel('Time')
plt.plot(x, bkems3, '-ks')
plt.plot(x, bksts3, '-k^')
plt.plot(x, bkems2, '-ks')
plt.plot(x, bksts2, '-k^')
plt.plot(x, bkems1, '-ks')
plt.plot(x, bksts1, '-k^')
plt.annotate('i=3', xy=(4600, 5000), xytext=(4800, 6400), arrowprops=dict(facecolor='black'))
plt.annotate('i=2', xy=(4800, 8500), xytext=(4800, 8600))
plt.annotate('i=1', xy=(4800, 10300), xytext=(4800, 10400))
plt.grid()
plt.axis([2500, 5000, 3500, 11500])
plt.savefig('bks.png')
# plt.show()
plt.close()

gwems3 = [5680, 6343, 6697, 6993, 7220, 7375]
gwsts3 = [7757, 8515, 9160, 9557, 9796, 9920]
gwems2 = [6989, 7843, 8435, 8997, 9431, 9809]
gwsts2 = [8782, 9811, 10655, 11287, 11913, 12333]
gwems1 = [8972, 9862, 10756, 11392, 12009, 12481]
gwsts1 = [9540, 10634, 11640, 12504, 13370, 14011]

plt.figure(3)
plt.xlabel('Network Size')
plt.ylabel('Time')
plt.plot(x, gwems3, '-ks')
plt.plot(x, gwsts3, '-k^')
plt.plot(x, gwems2, '-ks')
plt.plot(x, gwsts2, '-k^')
plt.plot(x, gwems1, '-ks')
plt.plot(x, gwsts1, '-k^')
plt.annotate('i=3', xy=(4600, 7600), xytext=(4800, 8400), arrowprops=dict(facecolor='black'))
plt.annotate('i=2', xy=(4800, 10800), xytext=(4800, 11000))
plt.annotate('i=1', xy=(4800, 12700), xytext=(4800, 13000))
plt.grid()
plt.axis([2500, 5000, 5600, 14100])
plt.savefig('gws.png')
# plt.show()
plt.close()

emm3 = [422, 583, 703, 816, 852, 1962]
bam3 = [967, 1257, 1412, 1548, 1653, 1737]
emm2 = [1011, 1447, 1516, 1603, 1723, 1793]
bam2 = [1246, 1511, 1704, 1871, 1996, 2089]
emm1 = [1707, 1689, 1791, 1907, 2055, 2226]
bam1 = [1445, 1780, 1965, 2139, 2293, 2400]

plt.figure(4)
plt.xlabel('Network Size')
plt.ylabel('Time Slots')
plt.plot(x, emm3, '-ks')
plt.plot(x, bam3, '-k^')
plt.plot(x, emm2, '-ks')
plt.plot(x, bam2, '-k^')
plt.plot(x, emm1, '-ks')
plt.plot(x, bam1, '-k^')
plt.annotate('i=3', xy=(4600, 1300), xytext=(4800, 1400), arrowprops=dict(facecolor='black'))
plt.annotate('i=2', xy=(4800, 1800), xytext=(4800, 1900))
plt.annotate('i=1', xy=(4800, 2150), xytext=(4800, 2250))
plt.grid()
plt.axis([2500, 5000, 400, 2400])
plt.savefig('embam.png')
# plt.show()
plt.close()

bkemm3 = [963, 1174, 1341, 1477, 1574, 1743]
bkstm3 = [1121, 1359, 1515, 1663, 1768, 1852]
bkemm2 = [1259, 1472, 1650, 1812, 1940, 2014]
bkstm2 = [1356, 1598, 1792, 1944, 2046, 2133]
bkemm1 = [1453, 1688, 1909, 2047, 2155, 2220]
bkstm1 = [1594, 1832, 2057, 2204, 2333, 2424]

plt.figure(5)
plt.xlabel('Network Size')
plt.ylabel('Time Slots')
plt.plot(x, bkemm3, '-ks')
plt.plot(x, bkstm3, '-k^')
plt.plot(x, bkemm2, '-ks')
plt.plot(x, bkstm2, '-k^')
plt.plot(x, bkemm1, '-ks')
plt.plot(x, bkstm1, '-k^')
plt.annotate('i=3', xy=(4600, 1650), xytext=(4800, 1750), arrowprops=dict(facecolor='black'))
plt.annotate('i=2', xy=(4800, 1950), xytext=(4800, 2050))
plt.annotate('i=1', xy=(4800, 2200), xytext=(4800, 2300))
plt.grid()
plt.axis([2500, 5000, 950, 2450])
plt.savefig('bkm.png')
# plt.show()
plt.close()

gwemm3 = [1051, 1261, 1422, 1557, 1605, 1745]
gwstm3 = [1332, 1560, 1701, 1811, 1896, 1946]
gwemm2 = [1439, 1698, 1907, 2054, 2169, 2202]
gwstm2 = [1643, 1927, 2176, 2364, 2527, 2601]
gwemm1 = [1766, 1988, 2203, 2340, 2449, 2502]
gwstm1 = [1840, 2126, 2391, 2579, 2762, 2845]

plt.figure(6)
plt.xlabel('Network Size')
plt.ylabel('Time Slots')
plt.plot(x, gwemm3, '-ks')
plt.plot(x, gwstm3, '-k^')
plt.plot(x, gwemm2, '-ks')
plt.plot(x, gwstm2, '-k^')
plt.plot(x, gwemm1, '-ks')
plt.plot(x, gwstm1, '-k^')
plt.annotate('i=3', xy=(4600, 1650), xytext=(4800, 1750), arrowprops=dict(facecolor='black'))
plt.annotate('i=2', xy=(4800, 2200), xytext=(4800, 2300))
plt.annotate('i=1', xy=(4800, 2600), xytext=(4800, 2700))
plt.grid()
plt.axis([2500, 5000, 1000, 2900])
plt.savefig('gwm.png')
# plt.show()
plt.close()