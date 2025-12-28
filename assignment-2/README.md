# Assignment_2 Project

##  Overview
This project demonstrates the basic usage of IPFS (InterPlanetary File System) to store and retrieve artifacts in a decentralized manner. A local IPFS node is 
initialized, a file is uploaded to IPFS, and the same file is retrieved using its Content Identifier (CID)

## TO Execute This
### Initialize IPFS node
ipfs init

### Start the IPFS daemon 
ipfs daemon

### Add a file to IPFS
ipfs add <filename>

We will get CID when we add a file to IPFS

### Retrieve the file using CID
ipfs cat <CID>

##Explaination
When a file is added to IPFS, it is broken into chunks, hashed, and assigned a CID.The CID uniquely represents the file’s content, not its location. 
Retrieving the file using the CID fetches the exact data from the IPFS network.IPFS ensures data integrity because any change in file content results in
a different CID, making tampering immediately detectable.
