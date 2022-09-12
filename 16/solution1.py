import sys

VERSION_LENGTH = 3
TYPE_LENGTH = 3
ID_INDEX = 6
SUB_PACKETS_LENGTH = 15
ADDITIONAL_INFO_START_INDEX = 7
SUB_PACKETS_NUMBER = 11

hex_dic = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111"
}

# Returns version and lenght
def parse_literal_packet(packet):

    is_last_group = False
    sub_group_start_index = (VERSION_LENGTH + TYPE_LENGTH)
    version = int(packet[0: VERSION_LENGTH], 2)
    
    while not is_last_group:
    
        sub_group_start_bit = packet[sub_group_start_index]
        if sub_group_start_bit == "0":
            is_last_group = True
        
        sub_group_start_index += 5
    
    return (version, sub_group_start_index)
    
def parse_operator_packet(packet):
    
    version = int(packet[0: VERSION_LENGTH], 2)
    print("operator type", type)
    length_id = packet[ID_INDEX]

    if length_id == "0":
        print("length id 0")
        sub_packets_len = get_sub_packets_length(packet)
        print("sub packet len", sub_packets_len)
        packets_start_index = (ADDITIONAL_INFO_START_INDEX + SUB_PACKETS_LENGTH)
        sub_sum_version, length = parse_bits_delimited_packets(packet[packets_start_index:], sub_packets_len)
        return (sub_sum_version + version, length + packets_start_index)
        
        
    elif length_id == "1":
        print("length id 1")
        sub_packets_num = get_sub_packets_number(packet)
        print("length", sub_packets_num)
        packets_start_index = (ADDITIONAL_INFO_START_INDEX + SUB_PACKETS_NUMBER)
        sub_sum_version, length = parse_number_delimited_packets(packet[packets_start_index:], sub_packets_num)
        return (sub_sum_version + version, length + packets_start_index)

    else:
        raise

def get_sub_packets_number(packet):
    number = packet[ADDITIONAL_INFO_START_INDEX: ADDITIONAL_INFO_START_INDEX + SUB_PACKETS_NUMBER]
    return int(number, 2)

def get_sub_packets_length(packet):
    number = packet[ADDITIONAL_INFO_START_INDEX: ADDITIONAL_INFO_START_INDEX + SUB_PACKETS_LENGTH]
    return int(number, 2)

#returns value_sum and length
def parse_number_delimited_packets(packets, number_of_packets):

    packet_number = 0
    packet_start_index = 0
    version_sum = 0

    while packet_number < number_of_packets:
    
        print("parse packet", packet_number)
        packet_number += 1
        type = packets[packet_start_index + VERSION_LENGTH: packet_start_index + VERSION_LENGTH + TYPE_LENGTH]
        print("typee", type)
        
        
        if type == "100":
            literal_version, literal_length = parse_literal_packet(packets[packet_start_index:])
            packet_start_index += literal_length
            version_sum += literal_version
        
        else:
            operator_version, operator_length = parse_operator_packet(packets[packet_start_index:])
            print("version", operator_version, "leng", operator_length)
            version_sum += operator_version
            packet_start_index += operator_length
            
    return (version_sum, packet_start_index)

def parse_bits_delimited_packets(packets, packets_len):

    print("packets", packets)
    packet_start_index = 0
    version_sum = 0
    
    while packet_start_index < packets_len:
    
        type = packets[packet_start_index + VERSION_LENGTH: packet_start_index + VERSION_LENGTH + TYPE_LENGTH]
        print("type", type)
        
        if type == "100":
            literal_version, literal_length = parse_literal_packet(packets[packet_start_index:])
            version_sum += literal_version
            packet_start_index += literal_length
            print("literal version", literal_version)
            print("literal length", literal_length)
        
        else:
            operator_version, operator_length = parse_operator_packet(packets[packet_start_index:])
            version_sum += operator_version
            packet_start_index += operator_length
                    
    return (version_sum, packet_start_index)
                
                
def solution_1(packet):

    version = packet[0:VERSION_LENGTH]
    type = packet[VERSION_LENGTH: VERSION_LENGTH + TYPE_LENGTH]
    
    if type == "100":
        return int(version, 2)
    
    else:
        operator_version, _ = parse_operator_packet(packet)
        return operator_version


def convert_to_binary(input):
    input_len = len(input)
    binary_string = ""
    
    for hex in input:
        binary_string += hex_dic[hex]
    return binary_string
    
def main():
    if len(sys.argv) < 2:
        print("missing args")
        return
    
    filename = sys.argv[1]
    f = open(filename, "r")
    line = f.readlines()[0]
    converted_input = convert_to_binary(line)
    print("converted input", converted_input)
    print(solution_1(converted_input))

main()


