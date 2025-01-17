import sapien
urdf_file = sapien.asset.download_partnet_mobility(179, token)
# create scene and URDF loader
urdf_loader.load(urdf_file)