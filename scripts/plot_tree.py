#!/usr/bin/env python
#coding=utf8
import os
import sys
import subprocess
from scipy import spatial

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print '	 python plot_tree.py NODE'
		sys.exit()

	fuzz_home = os.path.join(os.path.expanduser('~'), './GreedyFuzzing/fuzz/')
	node_dir = os.path.join(fuzz_home, sys.argv[1])
	queue_dir = os.path.join(node_dir, './output/queue')
	crashes_dir = os.path.join(node_dir, './output/crashes')
	hangs_dir = os.path.join(node_dir, './output/hangs')
	memory_trace_file = os.path.join(node_dir, './output/memory_traces.txt')
	path_trace_file = os.path.join(node_dir, './output/path_traces.txt')
	output_file = os.path.join(node_dir, sys.argv[1]+'.csv')

	mem_traces = {}
	with open(memory_trace_file, 'r') as ifile:
		lines = ifile.readlines()
		for x in lines:
			y = x.strip(', \n').split(',')
			fname = y[0]
			f_type = 'Crash' if 'crashes' in fname else ('Hang' if 'hangs' in fname else '')
			fname = fname[fname.rfind('/')+1:]
			fname = f_type+':'+fname if len(f_type) > 0 else fname
			mem_traces[fname] = [int(k) for k in y[1:]]

	path_traces = {}
	with open(path_trace_file, 'r') as ifile:
		lines = ifile.readlines()
		for x in lines:
			y = x.strip(', \n').split(',')
			fname = y[0]
			f_type = 'Crash' if 'crashes' in fname else ('Hang' if 'hangs' in fname else '')
			fname = fname[fname.rfind('/')+1:]
			fname = f_type+':'+fname if len(f_type) > 0 else fname

			trace = [0]*(1<<16)
			for z in y[1:]:
				splits = z.split(':')
				if len(splits) != 2:
					break
				trace[int(splits[0], 16)] = int(splits[1], 16)
			path_traces[fname] = trace

	all_fnames = [x.replace(',', '#') for x in os.listdir(queue_dir) if x.startswith('id:')]
	all_fnames.extend(['Crash:'+x.replace(',', '#') for x in os.listdir(crashes_dir) if x.startswith('id:')])
	all_fnames.extend(['Hang:'+x.replace(',', '#') for x in os.listdir(hangs_dir) if x.startswith('id:')])

	f_parent = {}
	for x in all_fnames:
		src = ''
		if 'src:' in x:
			src_start = x.find('src:') + 4
			src_end = x.find('#', src_start)
			src = x[src_start:src_end]
			src = src[:src.find('+')] if '+' in src else src

		if len(src) <= 0:
			f_parent[x] = 'v_root'
		else:
			f_parent[x] = next((k for k in all_fnames if k.startswith('id:'+src)), 'v_root')

	with open(output_file, 'wb') as ofile:
		ofile.write('id,fname,crash,hang,path_dist,malloc_dist,free_dist,load_dist,store_dist\n')
		ofile.write('v_root,v_root,N,N,NA,NA,NA,NA,NA\n')

		for x in all_fnames:
			parents = x[:x.find('#')]
			cur = x
			while cur in f_parent:
				cur = f_parent[cur]
				parents = (cur[:cur.find('#')] + '.' + parents) if '#' in cur else (cur + '.' + parents)

			parents = parents.replace(':', '-')

			crash = 'Y' if x.startswith('Crash') else 'N'
			hang = 'Y' if x.startswith('Hang') else 'N'

			path_dist = float('-inf')
			malloc_dist = 0
			free_dist = 0
			load_dist = 0
			store_dist = 0

			if x in f_parent:
				p = f_parent[x]
				path_dist = spatial.distance.cosine(path_traces[x], path_traces[p]) if (x in path_traces and p in path_traces) else float("-inf")
				malloc_dist = (mem_traces[x][1]-mem_traces[p][1]) if (x in mem_traces and p in mem_traces) else 0
				free_dist = (mem_traces[x][5]-mem_traces[p][5]) if (x in mem_traces and p in mem_traces) else 0
				load_dist = sum([1 if (mem_traces[x][k] != 0 and mem_traces[p][k] == 0) else 0 for k in range(68, 122)]) if (x in mem_traces and p in mem_traces) else 0
				store_dist = sum([1 if (mem_traces[x][k] != 0 and mem_traces[p][k] == 0) else 0 for k in range(123, 177)]) if (x in mem_traces and p in mem_traces) else 0

			ofile.write('%s,%s,%s,%s,%f,%d,%d,%d,%d\n' % ( \
						parents, \
						x, \
						crash, \
						hang, \
						path_dist, \
						malloc_dist, \
						free_dist, \
						load_dist, \
						store_dist))

	cmd = 'scp -r ' + output_file + ' desk:/var/www/figs'
	print cmd
	subprocess.Popen(cmd, shell=True)
	print 'Access: 156.56.159.155:9100/status.html?csv=./figs/%s.csv' % sys.argv[1]
