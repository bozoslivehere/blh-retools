import idc
import idaapi

# ais = Address In Segment
# TODO: Also dump metadata file (make optional?)
def DumpSegment(ais):
	SegmentStart = idc.GetSegmentAttr(ais, idc.SEGATTR_START)
	SegmentSize = idc.GetSegmentAttr(ais, idc.SEGATTR_END) - SegmentStart
	SegmentName = idc.SegName(ais)
	SegmentData = idc.GetManyBytes(SegmentStart, SegmentSize, True)
	FileName = SegmentName + "-%X-%X" % (SegmentStart,SegmentStart+SegmentSize) + ".dmp"

	f = open(FileName, 'wb+')
	f.write(SegmentData)
	f.close()

	print "Dumped 0x%X" % SegmentSize + " bytes into " + FileName
	