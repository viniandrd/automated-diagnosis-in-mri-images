config = dict()

# BraTS19 dataset path (extracted once)
config['dataset_path'] = 'D:/ViniAndrade/TCC/ConjuntodeDados/BraTS19/training/'

# Path for images extraction
config['images_path'] = 'D:/ViniAndrade/TCC/ConjuntodeDados/BraTS19 PNG 70-120 4/'

# Which MR modality extract
config['modality'] = 't1c'

# Extract slices starting from
config['initial_slice'] = 70

# Extract slices until
config['final_slice'] = 120

# Input shape for segmentation_models
config['input_shape'] = (None, None, 1)

# Epochs for training models
config['epochs'] = 100

# Batch size
config['batch_size'] = 16

# Path to save results (weights, training history, graphics)
config['save_dir'] = ''

# Input shape of the models
config['image_shape'] = (128, 128)

# Classes of the mask
config['classes'] = 4

# Ouput for saving ground truth of test set
config['out_test'] = './test_set/'