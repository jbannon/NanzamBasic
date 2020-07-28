"""
CONSTANTS TO BE USED


"""


""" SYSTEM-LEVEL CONSTANTS """
SYSTEM_BINS = "../bin/"  # location to store important binaries for the system
PARAM_PATH = "../params/" # location to store parameter files
ALU_SRC = "../data/meta/alu.txt" #source of alu sequence
MACHINE_LIMIT=10**5 # largest molecule length machine can handle
FIG_PATH = "../figs/"

""" IN-SILICO SIMULATION CONSTANTS """


tloc_sim_msg = """ 
	Simulating Patient Sequences from Reference Sequences 
		will generate reference files for both 
		wild type and translocated patient_seqs
	"""
MAX_WILD = 1 # controls fsa
SCALE = 1 # controls scale
#MAX_INSERT_LENGTH = 3 # test code
MAX_INSERT_LENGTH = 2*10**3


MIN_SIGMA = 0.1
MAX_SIGMA = 1.5


REF_SEQS  = "../data/seqs/ref_seqs/"
REF_MAPS = "../data/maps/ref_maps/"


PATIENT_SEQS = "../data/seqs/patient_seqs_small/"
#PATIENT_SEQS = "../data/seqs/patient_seqs/"

PATIENT_MAPS_C = "../data/maps/patient_maps_C/"
PATIENT_MAPS_IS= "../data/maps/patient_maps_IS/"
#PATIENT_MAPS = "../data/seqs/patient_maps/"




MapSim_msg = """Running Full Nanomapping Simulation Process
	Will create: 
		in silico reference maps (no noise)
		in silico patient maps (no noise)
		consensus patient maps (simulating real life data with noise estimated)
		"""


""" NANZAM CONSTANTS """

HASH_DEST = "../bin/"
NANZAM_msg = """ running nanzam unit tests"""

""" SIMPLISTIC ALPHABETS FOR SMALL BIN NUMBER CASES """
SIMPLE_ALPHS = {1:['M'],2:['S','L'],3:['S','M','L'],4:['S','M','L','X'],5:['T','S','M','L','X'],
			6:['T','S','M','L','X','Y'],7:['R', 'T','S','M','L','X','Y'],8:['R', 'T','S','M','L','X','Y','Z'],
			9:['Q','R', 'T','S','M','L','X','Y']}
NUM_RAND=10**3
MOLEC_LEN=3*10**5
MIN_K = 5
MAX_K = 10
STEP= 2

label_map={250:'250bp/',1000:'1kb/', 1*10**5:'100kb/', 2*10**5: '200kb/', 3*10**5:'300kb/', 5*10**5:'500kb/', 10**6 : '1Mb/'}
genome_sizes = [250,1000, 1*10**5, 2*10**5, 5*10**5, 10**6]

#TABLE_SIZE=2281
TABLE_SIZE=NUM_RAND