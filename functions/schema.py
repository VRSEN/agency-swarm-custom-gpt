from helpers import init_agency

if __name__ == '__main__':
    agency = init_agency("test")

    schema = agency.get_customgpt_schema("YOUR_FUNCTION_URL") # paste your url from terminal here

    # save to schema.json
    with open('schema.json', 'w') as outfile:
        outfile.write(schema)

    print("schema.json saved\n")

    print("Use these instructions to setup your agent in custom gpt:\n")

    print(agency.agents[0].instructions)