# Converter for the OrgaTalk LAN Party Database


## Supported input formats

* [DOTLAN Intranet](https://intranet.dotlan.net/) SQL dump
* [LANsuite](https://github.com/lansuite/lansuite) XML


## Installation

* [Install uv](https://docs.astral.sh/uv/) (if it isn't already installed)
* Clone repository: `git clone https://github.com/lanpartydb/tools.git`
* Enter converter path: `cd tools/converter`


## Usage


### For DOTLAN

* Export tables `events` and `event_location` (both structure and data,
  without compression) from the DOTLAN "Support Tools".
* `uv run convert-dotlan-sql --base-url 'https://www.lanparty.example' --output-path output events-and-locations.sql`


### For LANsuite

* An XML document with parties is publicly available at
  `https://www.yourparty.example/ext_inc/party_infos/infos.xml`.
* `uv run convert-lansuite-xml --output-path output infos.xml`


## License

MIT


## Author

Jochen Kupperschmidt
