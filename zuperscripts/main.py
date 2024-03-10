import argparse
import threading
import random
import time
from TransactionERC import TransactionERC
from TransactionNEAR import TransactionNear

def erc_threading(wallet_address, rpc_endpoint):

    """
    Function to Define Ethereum Transaction Thread Doing

    Arguments:
        wallet_address (str): Wallet address that we will check the balance for
        rpc_endpoint (str): RPC endpoint

    Returns:
        None
    """

    erc_tx_counter = 0

    while True:
        erc_tx_counter += 1
        print(f"Ethereum Transaction no. {erc_tx_counter} \n")

        TransactionERC(wallet_address, rpc_endpoint).check_balance()

        random_delay = random.randint(60, 90)
        print(f"Waiting for {random_delay} seconds...")
        print("=======================================================")

        time.sleep(random_delay)

def near_mainnet_threading(account_id, rpc_endpoint):

    """
    Function to Define NEAR Mainnet Transaction Thread Doing

    Arguments:
        account_id (str): Account ID that we will check the balance for
        rpc_endpoint (str): RPC endpoint

    Returns:
        None
    """

    near_mainnet_tx_counter = 0

    while True:
        near_mainnet_tx_counter += 1
        print(f"NEAR Mainnet Transaction no. {near_mainnet_tx_counter} \n")

        TransactionNear(account_id, rpc_endpoint).check_balance()

        random_delay = random.randint(60, 90)
        print(f"Waiting for {random_delay} seconds...")
        print("=======================================================")

        time.sleep(random_delay)

def near_testnet_threading(account_id, rpc_endpoint):

    """
    Function to Define NEAR Testnet Transaction Thread Doing

    Arguments:
        account_id (str): Account ID that we will check the balance for
        rpc_endpoint (str): RPC endpoint

    Returns:
        None
    """

    near_testnet_tx_counter = 0

    while True:
        near_testnet_tx_counter += 1
        print(f"NEAR Testnet Transaction no. {near_testnet_tx_counter} \n")

        TransactionNear(account_id, rpc_endpoint).check_balance()

        random_delay = random.randint(60, 90)
        print(f"Waiting for {random_delay} seconds...")
        print("=======================================================")

        time.sleep(random_delay)

def main():
    # Define Parser
    parser = argparse.ArgumentParser(description='Run transactions.')

    # Add Arguments
    parser.add_argument('--ethereum_rpc_endpoint', help='Ethereum RPC endpoint')
    parser.add_argument('--ethereum_wallet_address', help='Ethereum wallet address')
    parser.add_argument('--near_mainnet_rpc_endpoint', help='NEAR Mainnet RPC endpoint')
    parser.add_argument('--near_mainnet_account_id', help='NEAR Mainnet account ID')
    parser.add_argument('--near_testnet_rpc_endpoint', help='NEAR Testnet RPC endpoint')
    parser.add_argument('--near_testnet_account_id', help='NEAR Testnet account ID')

    # Parse Arguments
    args = parser.parse_args()

    # Start Ethereum Threads if RPC endpoint and wallet address are provided
    if args.ethereum_rpc_endpoint and args.ethereum_wallet_address:
        erc_thread = threading.Thread(target=erc_threading, args=(args.ethereum_wallet_address, args.ethereum_rpc_endpoint))
        erc_thread.start()
        time.sleep(1)
    else:
        print("Please provide Ethereum RPC endpoint and wallet address")
        print("=======================================================")

    # Start NEAR Mainnet Threads if RPC endpoint and account ID are provided
    if args.near_mainnet_rpc_endpoint and args.near_mainnet_account_id:
        near_mainnet_thread = threading.Thread(target=near_mainnet_threading, args=(args.near_mainnet_account_id, args.near_mainnet_rpc_endpoint))
        near_mainnet_thread.start()
        time.sleep(1)
    else:
        print("Please provide NEAR Mainnet RPC endpoint and account ID")
        print("=======================================================")

    # Start NEAR Testnet Threads if RPC endpoint and account ID are provided
    if args.near_testnet_rpc_endpoint and args.near_testnet_account_id:
        near_testnet_thread = threading.Thread(target=near_testnet_threading, args=(args.near_testnet_account_id, args.near_testnet_rpc_endpoint))
        near_testnet_thread.start()
        time.sleep(1)
    else:
        print("Please provide NEAR Testnet RPC endpoint and account ID")
        print("=======================================================")

if __name__ == "__main__":
    main()
