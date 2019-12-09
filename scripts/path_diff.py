#!/usr/bin/env python
#coding=utf8
import os
import sys
from scipy import spatial

path_1 = 'e2:1,334:2,3b7:1,52c:1,671:1,6cb:1,773:1,7db:8,851:10,9ce:1,9e9:8,cc0:1,ef1:1,efd:1,1089:1,1090:4,131e:1,1477:1,14f8:10,161f:1,1793:1,17e5:1,17f3:1,1a2b:1,1bc9:1,1d0b:40,1d8f:20,1e1d:1,1ecb:1,1f8b:4,2034:4,227b:4,238b:1,24cc:1,24e0:1,264a:1,26ed:1,27ea:1,289c:1,2943:1,297a:1,2dcf:1,2ddb:1,2e78:1,2f12:1,2fc4:1,3092:1,30c6:1,3230:8,3438:1,3465:1,34fa:1,3589:1,3619:1,362d:2,3664:1,36b6:4,3713:1,377b:1,389f:1,38a6:1,38ff:1,391a:1,3952:1,3963:1,397a:1,3a05:1,3b70:1,3bcd:1,3c3a:1,3c8d:8,3cee:1,3d4f:1,3e17:4,3f85:1,407a:1,4266:1,4304:1,4388:1,453b:8,4644:1,46d8:1,4745:1,4869:1,4873:1,49a2:1,49b6:4,4b69:4,4c2f:1,4c86:1,4ca7:8,4caa:1,4cc6:4,4cdd:1,4f21:10,518a:1,51a5:4,5452:1,5576:1,558b:1,5a69:1,5bb5:10,5c10:8,5fbc:1,5fcf:1,615d:1,61f2:1,6269:1,629a:1,62f3:1,6359:1,64c6:1,64e3:4,6747:1,6749:20,679c:1,6806:1,685c:1,68a6:1,694b:1,6956:20,698e:1,69ff:1,6a41:1,6ae2:1,6bed:1,6cb2:1,6da6:1,6f9a:1,6fdc:1,733e:1,7397:1,7483:2,74ee:1,753f:1,7582:1,76ad:1,7778:1,787d:1,7a2b:8,7c2f:1,7c6d:1,7ce5:1,7d0c:1,7e23:1,7eb5:1,7eee:1,806a:20,8167:1,822d:1,82af:1,8540:1,85d0:1,8665:1,8867:1,8952:4,8955:1,8b42:1,8b73:1,8da0:1,8e84:20,8eaa:1,8f56:1,8fbb:20,8fc2:1,8ff5:1,9042:1,9056:1,9118:8,92f8:1,92ff:8,94a9:1,951d:1,9583:1,95d3:40,9689:1,9738:1,999a:40,9c7f:40,9cd1:4,9e53:1,9eb4:1,a091:1,a12c:1,a257:1,a406:1,a4d9:1,a61c:1,a955:1,a9c4:10,abfe:1,ac78:1,ad40:1,ad60:1,b111:1,b125:8,b1f4:2,b37e:10,b3f8:1,b424:1,b49b:1,b587:1,b64a:1,b6f1:1,b7c5:1,b835:1,ba40:1,bb47:1,bbd8:1,bd07:1,bf58:1,bfb5:2,c04b:4,c053:1,c0e1:1,c1ec:2,c25a:8,c2ab:10,c2f1:4,c30d:1,c3c2:8,c3fb:1,c45c:1,c513:1,c54a:1,c736:1,c942:2,c956:2,c9f4:1,ca27:1,cbc3:2,cbef:1,cc06:8,cc74:1,cdc6:4,ce22:8,cf03:1,d03b:10,d0e0:1,d1cb:1,d4e8:1,d630:40,d668:10,d732:2,d78f:1,d846:20,d88f:40,d891:1,d8a8:2,da3a:10,db78:1,dbea:2,dc05:1,dc30:1,dccb:2,dccd:1,dd16:1,dec9:1,df3e:1,e0d6:1,e11b:1,e121:1,e18c:20,e214:1,e25f:1,e280:1,e53a:4,e5b1:1,e834:1,e905:1,e97c:1,e99a:10,ea35:40,eba4:1,ec29:1,ee32:1,eeb4:1,eee1:1,ef85:8,efff:1,f0da:1,f28d:1,f2dd:1,f4c7:1,f638:1,f722:1,f8eb:1,f9e4:1,fa7e:1,fad5:1,fadd:1,fbde:8,fc34:1,feb8:1,feda:1,ffb2:1'
path_2 = 'e2:1,334:2,3b7:1,52c:1,671:1,6cb:1,773:1,7db:8,851:10,9b0:1,9ce:1,9e9:8,cc0:1,ef1:1,efd:1,1089:1,1090:4,131e:1,1477:1,14f8:10,14fc:1,161f:1,1793:1,17e5:1,17f3:1,1a2b:1,1bc9:1,1d0b:40,1d8f:20,1e1d:1,1ecb:1,1f8b:4,2034:4,227b:4,238b:1,24cc:1,24e0:1,264a:1,26ed:1,27ea:1,2879:1,289c:1,2943:1,297a:1,2dcf:1,2ddb:1,2e78:1,2f12:1,2fc4:1,3092:1,30c6:1,3230:8,3438:1,3465:1,34fa:1,3589:1,3619:1,362d:2,3664:1,36b6:4,3713:1,377b:1,389f:1,38a6:1,38ff:1,391a:1,3952:1,3963:1,397a:1,3a05:1,3b70:1,3bcd:1,3c3a:1,3c8d:8,3cee:1,3d4f:1,3e17:4,3f85:1,407a:1,4266:1,4304:1,4388:1,453b:8,4644:1,46d8:1,4745:1,4869:1,4873:1,49a2:1,49b6:4,4b69:4,4c2f:1,4c86:1,4ca7:8,4caa:1,4cc6:4,4f21:10,518a:1,51a5:4,5452:1,5576:1,558b:1,5a69:1,5bb5:10,5c10:8,5fbc:1,5fcf:1,615d:1,61f2:1,6269:1,629a:1,62f3:1,6359:1,64c6:1,64e3:4,6579:1,6747:1,6749:20,679c:1,6806:1,685c:1,68a6:1,694b:1,6956:10,698e:1,69ff:1,6ae2:1,6bed:1,6cb2:1,6da6:1,6f9a:1,6fdc:1,733e:1,7397:1,7483:2,74ee:1,753f:1,7582:1,76ad:1,7778:1,787d:1,7a2b:8,7c2f:1,7ce5:1,7d0c:1,7e23:1,7eb5:1,7eee:1,806a:20,8167:1,822d:1,82af:1,8540:1,85d0:1,8665:1,8867:1,8952:4,8955:1,8b42:1,8b73:1,8da0:1,8e84:20,8eaa:1,8f56:1,8fbb:20,8fc2:1,8ff5:1,9042:1,9056:1,9118:8,92f8:1,92ff:8,94a9:1,951d:1,9583:1,95d3:40,9689:1,9738:1,999a:40,9c7f:40,9cd1:4,9e53:1,9eb4:1,a091:1,a12c:1,a257:1,a406:1,a4d9:1,a539:1,a61c:1,a822:1,a955:1,a9c4:10,abfe:1,ad40:1,ad60:1,b111:1,b125:8,b1f4:2,b37e:10,b3f8:1,b424:1,b49b:1,b587:1,b64a:1,b6f1:1,b7c5:1,b835:1,ba40:1,bb47:1,bbd8:1,bd07:1,bf58:1,bfb5:2,c04b:4,c053:1,c0e1:1,c1ec:2,c25a:8,c2ab:10,c2f1:4,c30d:1,c3c2:8,c3fb:1,c45c:1,c513:1,c54a:1,c736:1,c942:2,c956:2,c9f4:1,ca27:1,cb6d:1,cbc3:2,cbef:1,cc06:8,cc74:1,cdc6:4,ce22:8,cf03:1,d03b:10,d0e0:1,d1cb:1,d4e8:1,d630:40,d668:10,d732:2,d78f:1,d846:20,d88f:40,d891:1,d8a8:2,da3a:10,db78:1,dbea:2,dc05:1,dccb:2,dccd:1,dd16:1,dec9:1,df3e:1,e0d6:1,e11b:1,e121:1,e18c:10,e214:1,e25f:1,e280:1,e53a:4,e5b1:1,e834:1,e905:1,e97c:1,e99a:10,ea35:40,eba4:1,ec29:1,ee32:1,eeb4:1,eee1:1,ef85:8,efff:1,f0da:1,f28d:1,f2dd:1,f4c7:1,f638:1,f722:1,f8eb:1,f9e4:1,fa7e:1,fad5:1,fbde:8,feb8:1,feda:1,ffb2:1'

if __name__ == '__main__':
	trace_1 = [0]*(1<<16)
	trace_2 = [0]*(1<<16)

	for z in path_1.split(','):
		splits = z.split(':')
		if len(splits) != 2:
			break
		trace_1[int(splits[0], 16)] = int(splits[1], 16)

        for z in path_2.split(','):
                splits = z.split(':')
                if len(splits) != 2:
                        break
                trace_2[int(splits[0], 16)] = int(splits[1], 16)

	print 'path cosine dist %f' % spatial.distance.cosine(trace_1, trace_2)

	uniq_1 = sum([1 if trace_1[i] > trace_2[i] else 0 for i in range(len(trace_1))])
	uniq_2 = sum([1 if trace_2[i] > trace_1[i] else 0 for i in range(len(trace_2))])

	print 'uniq_1 %d, uniq_2 %d' % (uniq_1, uniq_2)
