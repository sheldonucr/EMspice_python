import numpy as np
import os
class tree:
	def __init__(self,branch_num,branch_name, branch_length, branch_width,branch_curden):
		self.branch_num = branch_num
		self.branch_name = branch_name.copy()
		self.branch_length = branch_length.copy()
		self.branch_width = branch_width.copy()
		self.branch_curden = branch_curden.copy()
def get_constant(constant_file):
	with open (constant_file, 'r') as f:
		EM_constants = f.readlines()
		T = float(EM_constants[0].split(',')[-1])
		D0 = float(EM_constants[1].split(',')[-1])
		E = float(EM_constants[2].split(',')[-1])
		Ea_ratio = float(EM_constants[3].split(',')[-1])
		Ea = Ea_ratio * E
		kB = float(EM_constants[4].split(',')[-1])
		Da = D0 * np.exp(-Ea/(kB * T))
		B0 = float(EM_constants[5].split(',')[-1])
		Omega = float(EM_constants[6].split(',')[-1])
		cu_res = float(EM_constants[7].split(',')[-1])
		hCu = float(EM_constants[8].split(',')[-1])
		Ta_res = float(EM_constants[9].split(',')[-1])
		hTa = float(EM_constants[10].split(',')[-1])
		Z = float(EM_constants[11].split(',')[-1])
		kappa = (Da * B0 * Omega) / (kB*T)
		nx = float(EM_constants[12].split(',')[-1]) # the number of pieces of fdm
		wire_length = float(EM_constants[13].split(',')[-1])
		t_total = float(EM_constants[14].split(',')[-1])# normalized total time
		tstep = float(EM_constants[15].split(',')[-1]) # normalized tstep
		tstamp = [] # every time step point
		for i in range(int(t_total/tstep)):
			tstamp.append(i*tstep)
		
	return T, D0, E, Ea, kB, Da, B0, Omega, cu_res, hCu, Ta_res, hTa, Z, kappa,nx,wire_length, t_total, tstep,tstamp   
def run_emcmd(input_spice):
	cmd = "./em_cmd " + input_spice
	#os.system(cmd)	
def get_all_width(tree_width):
	all_branch_width =[] 
	with open(tree_width, 'r') as f:
		all_branch_width_origin = f.readlines()
		for branch_width_origin in all_branch_width_origin:
			branch_width = branch_width_origin[1:]
			all_branch_width.append(float(branch_width))
	return all_branch_width 
def get_all_curden(tree_curden):
	all_branch_curden = []
	with open(tree_curden, 'r') as f:
		all_branch_curden_origin = f.readlines()
		for branch_curden_origin in all_branch_curden_origin:
			branch_curden = branch_curden_origin.split()[-1]
			all_branch_curden.append(float(branch_curden))
	return all_branch_curden 
def get_all_leng(tree_leng):
	all_branch_leng = []
	with open(tree_leng, 'r') as f:
		all_branch_leng_origin = f.readlines()
		for branch_leng_origin in all_branch_leng_origin:
			branch_leng = branch_leng_origin[1:]
			all_branch_leng.append(float(branch_leng))
	return all_branch_leng 	 
def gettree(tree_info,tree_width, tree_curden, tree_leng):
	all_branch_width = get_all_width(tree_width)
	all_branch_curden = get_all_curden(tree_curden)
	all_branch_leng = get_all_leng(tree_leng)
	tree_list = gettree_info(tree_info, all_branch_width, all_branch_curden, all_branch_leng)
	
	return tree_list
def get_one_branch_name(line):
	name = line.split()[0]
	return name
def gettree_info(tree_info, all_branch_width, all_branch_curden, all_branch_leng):
	tree_list  = []
	branch_name = [] # branch name of a tree
	branch_num = 0 # number of branch of a tree
	branch_counter = 0 # branch counter of the file		
	branch_length = [] 
	branch_width = []
	branch_curden = []
	with open (tree_info, 'r') as f:
		lines = f.readlines()
		for line in lines:
			if line.split()[0] == 'xx':
				newtree = tree(branch_num,branch_name, branch_length, branch_width,branch_curden)
				tree_list.append(newtree)
				branch_name = [] # branch name of a tree
				branch_num = 0 # number of branch of a tree
				branch_length = [] 
				branch_width = []
				branch_curden = []
			else:	
				one_branch_name = get_one_branch_name(line)
				branch_name.append(one_branch_name)
				branch_num = branch_num + 1
				branch_length.append(all_branch_leng[branch_counter])
				branch_width.append(all_branch_width[branch_counter])
				branch_curden.append(all_branch_curden[branch_counter])
				branch_counter = branch_counter + 1
	return 	tree_list			
#def get_tree_width(tree_width,tree_num):
#	brchwidth = [0] * tree_nnum
#	brch
#def init_parameters(treenum,initC,void,Lvoid, Lvoid1,Lvoid2,max_stress,max_stress_location,nx_total):
#	for i in range (treenum):
#		initC.append([])
#		void.append(0)
#		Lvoid.append(0)
#		Lvoid1.append(0)
#		Lvoid2.append(0)
#		max_stress.append(0)
#		max_stress_location.append(0)
#		nx_total.append(nx * brchnum[i]) - (nrchnum(i) - 1)
#		for j in range(nx_total[i]):
#			initC[i].append(0)
#		initC.append(nx_total)
#	Lvoid_last = Lvoid.copy
#	Lvoid_last1 = Lvoid1.copy
#	Lvoid_last2 = Lvoid2.copy
#
#	return initC, void, Lvoid, Lvoid1, Lvid2, max_stress, max_stress_location, nx_total, initC, Lvoid_last, Lvoid_last1, Lvoid_last2
#def simulation_process(init_flag, treenum, initC,void,Lvoid, Lvoid1,Lvoid2,max_stress,max_stress_location,nx_total, iterIdx):
#	if init_flag == 1:
#		initC = []
#		void = []
#		Lvoid = []
#		Lvoid1 = []
#		Lvoid2 = []
#		max_stress = []
#		max_stress_location = []
#		nx_total = []
#		init_parameters(treenum,initC,void,Lvoid, Lvoid1,Lvoid2,max_stress,max_stress_location,nx_total)
#		init_flag = 0
	# file name to store stress, curden and Lvoid
#	fname1 = 'u_stress_' + str(iterIdx) + '.txt'
#	fname2 = 'u_curden_' + str(iterIdx) + '.txt'
#	fname3 = 'u_Lvoid_' + str(iterIdx) + '.txt'
#	fid_resis = 'u_resis.txt'
#	for i in range(treenum):
#		Lvoid0 = 0
#		Lvoid01 = 0
#		Lvoid02 = 0
#		Lvoid_temp = 0
		#for k in range(brchnum[i])
#		FEM_run = 1
#		for j in range(FEM_run):
#			if void[i] == 0:
#				G,C,B = matrix_formation(nx,wires[i], J_list_norm[i])	
def matrix_formation(nx,wires0, J_list_norm0):
	wires = wires0.copy()
	J_list_norm = np.asarray(J_list_norm0)
	#wires[0] holds the name of a wire
	#wires[1] holds the name of the net the wire is associated with
	#wires[2] holds the x value of starting nodes
	#wires[3] holds the y value of starting nodes
	#wires[4] holds the names of the net the wires are assocaited with
	#wires[5] holds the x valye of destination nodes	
	#wires[6] holds the y value of destination nodes
	#wires[7] Resistance of wires
	n_wires = len(wires[0])
	w_lengs = np.zeros(n_wires,2)
	for n in range(n_wires):
		xL = abs(wires[5][n] - wires[2][n])
		if xL > 0:
			w_lengs[n][0] = xL
			w_lengs[n][1] = 1
		else:
			yL = wires[6][n] - wires[3][n]
			if yL >0:
				w_lengs[n][0] = yL
				w_lengs[n][1] = 2
			
	ys = wires[6]
	yn = ys - min(ys)
	num_Junctions = n_wires - 1
	nx = nx0
	nx_total = (nx * n_wires) - num_Junctions
	
	G = np.zeros([nx_total,nx_total])
	B = np.zeros([nx_tptal,n_wires])
	for i in range(1,(nx_total - 1)):
		G[i,i-1] = G[i,i-1] + 1
		G[i,i] = G[i,i] - 2
		G[i,i + 1] = G[i,i + 1] + 1
	G[0,0] = G[0,0] - 1
	G[0,1] = G[0,1] + 1
	G[-1,-1] = G[-1,-1] - 1
	G[-1,-2] = G[-1,-2] + 1
	index = 1
	t = np.zeros[1,n_wires]
	for i in range(n_wires):
		B[index,i] = 1
		B[index + nx - 1, i] = -1
		index = index + nx - 1;
	C = np.ones([nx_total])
	dx = 1/(nx_total - 1)
		
	return G, C, B
	
def onestep_simulation(T, D0, E, Ea, kB, Da, B0, Omega, cu_res, hCu, Ta_res, hTa, Z, kappa ,nx,wire_length, t_total, tstep,tstamp,tstamp_flag,stop_flag, cdnum, cdlist,init_flag, iterIdx, input_spice):
	run_emcmd(input_spice)
	tree_info = "tree_info.txt"
	tree_width = "tree_width.txt"
	tree_curden = "tree_curden.txt"
	if init_flag == 1:
		tree_leng = "tree_leng.txt"
	else:
		tree_leng = "tree_leng1.txt"
	tree_list = gettree(tree_info, tree_width, tree_curden, tree_leng) # tree_list is a list of tree structure.
	tree_stress = []
	if os.path.isfile('u_stress.txt'):
		print ("have initial stress")
		u_stress = "u_stress.txt"	
		tree_stress = get_stress_from_file(u_stress)
			
	else:
		tree_stress = getinitialstreee(tree_list, nx)
	print(len(tree_stress))
	if os.path.isfile('Void.txt'):
		print("t")
		Void_position, Void_length = getinitialvoid('Void.txt', "Lvoid.txt")
	else:
		Void_position = [] # for each tree, number of zero = branch number 0 means no void, 1 means void is on the left, -1 means on the write
		Void_length = [] # length of void on the branch, if 0 means no void.	
		for i in range (len(tree_list)):
			Void_position.append([])
			Void_length.append([])
			for j in range (tree_list[i].branch_num):
				Void_position[i].append(0)
				Void_length[i].append(0)
		with open('Void.txt', 'w') as positionfile:
			positionfile.writelines('\t'.join(str(j) for j in i) + '\n' for i in Void_position) 

	print(len(Void_position[-1]))
	print(len(Void_length[-1]))		
			
	#clean_repo(tree_info, tree_width, tree_curden,tree_leng)
	#simulation_process(tree_list) 		
def get_stress_from_file(u_stress):
	tree_stress = []
	with open (u_stress, 'r') as f:
		line_num = 0
		line = f.readline()
		line_sp = line.split()
		name = line_sp[0]
		tree_name = name.split("-")[0] + "-" + name.split("-")[1]
		
		current_tree_name = tree_name
		one_tree_stress = []
		while line:
			line_sp = line.split()
			if len(line_sp) == 2:
				name = line_sp[0]
				tree_name = name.split("-")[0] + "-" + name.split("-")[1]
				if tree_name != current_tree_name:
					tree_stress.append(one_tree_stress)
					one_tree_stress = []
					current_tree_name = tree_name
				stress = line_sp[1]
				one_tree_stress.append(stress)
			else:
				stress = line_sp[0]
				one_tree_stress.append(stress)

	
			line = f.readline()
	return tree_stress				
def getinitialstreee(tree_list,nx):
	# set all 0 for initial stress
	tree_stress = []
	for i in range(len(tree_list)):
		one_tree_stress = []
		branch_num = tree_list[i].branch_num
		stress_num = int(branch_num * (nx -1) + 1)
		for i in range(stress_num):
			one_tree_stress.append(0) # add initial stress for nodes.
		tree_stress.append(one_tree_stress)	
	return tree_stress	
def clean_repo(tree_info, tree_width, tree_curden,tree_leng):
	os.remove(tree_info)
	os.remove(tree_width)
	os.remove(tree_curden)
	os.remove(tree_leng)

def EM_simulation(T, D0, E, Ea, kB, Da, B0, Omega, cu_res, hCu, Ta_res, hTa, Z, kappa ,nx,wire_length, t_total, tstep,tstamp,input_spice):
	tstamp_flag = 1
	stop_flag = 0
	cdnum = int(t_total/tstep)
	cdlist = [1] * cdnum
	init_flag = 1
	interIdx = 0 
	pwl = cdlist.copy()
	for i in range(1):
		if stop_flag == 1:
			break
		onestep_simulation(T, D0, E, Ea, kB, Da, B0, Omega, cu_res, hCu, Ta_res, hTa, Z, kappa ,nx,wire_length, t_total, tstep,tstamp,tstamp_flag,stop_flag, cdnum, cdlist,init_flag, i, input_spice)	

if __name__ == '__main__':
	constant_file = "EM_spice_constant.txt"
	input_spice = "armcore.sp"	
	T, D0, E, Ea, kB, Da, B0, Omega, cu_res, hCu, Ta_res, hTa, Z, kappa ,nx,wire_length, t_total, tstep,tstamp = get_constant(constant_file)
	EM_simulation(T, D0, E, Ea, kB, Da, B0, Omega, cu_res, hCu, Ta_res, hTa, Z, kappa ,nx,wire_length, t_total, tstep,tstamp,input_spice )
		

