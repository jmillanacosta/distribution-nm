This repository makes an RDF (TBD) out of the supplementary materials to  Kumar _et al_, 2023: [Nanoparticle biodistribution coefficients: A quantitative approach for understanding the tissue distribution of nanoparticles](https://doi.org/10.1016/j.addr.2023.114708), which describe the observed %ID/g of nanoparticles at different time points for different organs and organisms.

## Information retrieval/question answering using LLMs:

Some notebooks use large language models to try to assess their performance in Information Retrieval, using the article's curated dataset as a control for human curated data.

### OpenAI's GPT-3.5 Turbo

Notebook [01_nanodistribution-openai-qa.ipynb](https://github.com/jmillanacosta/distribution-nm-rdf/blob/master/notebooks/01_nanodistribution-openai-qa.ipynb) uses the OpenAI API to answer the following questions for each available open access article reviewed by  Kumar _et al_, 2023:

```
Scan the following scientific article {full text/abstract} describing the use of animal models to investigate nanomaterial or nanoparticle biodistribution in organs to fill up the braces for each value (use 3 words max for each)

{full text/abstract}:
\"\"\"
{text}
\"\"\"

Your response:

1. assessed nanomaterial (exclude ligand): []
2. species of the animal model used for the in vivo assay: []
3: Strain of the animal model used for the in vivo assay: []
4. labelling used for the in vivo assay: []
5. analysis method used for measurements for the in vivo assay: []
6. Time points included in the in vivo assay (h): []
7: Organs analyzed: []
8: Nanomaterial shape: []
9: Nanomaterial type (lipid, silica, graphene, gold, metal oxide...): []
10: Nanomaterial size (nm): []
11: Ligand used for imaging: []
```

Some big issues I see with the approach are:
- The chat model does not provide a scoring system for the provided answers, neither are the parameters of the model fully known
- The model is set to `temperature=0` to try to get the most deterministic answer possible, but a different answer is possible at each round
- Data still needs to be curated afterwards, since the model does not stick to a specific lexicon -i.e., strains of mice reported correctly but inconsistently as follows:

<table>
	<tbody>
		<tr>
			<td><p>pmcid</p>
			</td>
			<td><p>curated_strain</p>
			</td>
			<td><p>abs_strain</p>
			</td>
			<td><p>ft_strain</p>
			</td>
		</tr>
		<tr>
			<td><p>PMC3985880</p>
			</td>
			<td><p>Nude mice</p>
			</td>
			<td><p>U87MG tumor-bearing mice</p>
			</td>
			<td><p>U87MG tumor-bearing mice, nude mice</p>
			</td>
		</tr>
		<tr>
			<td><p>PMC4358630</p>
			</td>
			<td><p>Balb/c mice</p>
			</td>
			<td><p>EMT6 breast cancer model</p>
			</td>
			<td><p>BALB/c</p>
			</td>
		</tr>
		<tr>
			<td><p>PMC3211348</p>
			</td>
			<td><p>SCID mice</p>
			</td>
			<td><p>not specified</p>
			</td>
			<td><p>severe combined immune deficient (SCID) mice</p>
			</td>
		</tr>
		<tr>
			<td><p>PMC3492114</p>
			</td>
			<td><p>Male ddY mice</p>
			</td>
			<td><p>tumor-bearing mice</p>
			</td>
			<td><p>tumor-bearing mice</p>
			</td>
		</tr>
		<tr>
			<td><p>PMC3425121</p>
			</td>
			<td><p>Nude mice</p>
			</td>
			<td><p>not specified</p>
			</td>
			<td><p>athymic nude mice</p>
			</td>
		</tr>
		<tr>
			<td><p>PMC5039679</p>
			</td>
			<td><p>Nude mice</p>
			</td>
			<td><p>N/A</p>
			</td>
			<td><p>not specified</p>
			</td>
		</tr>
		<tr>
			<td><p>PMC4207078</p>
			</td>
			<td><p>Kunming mice</p>
			</td>
			<td><p>not specified</p>
			</td>
			<td><p>not specified</p>
			</td>
		</tr>
		<tr>
			<td><p>PMC4262629</p>
			</td>
			<td><p>Nude mice</p>
			</td>
			<td><p>U87MG</p>
			</td>
			<td><p>U87MG tumor-bearing mice, female athymic nude...</p>
			</td>
		</tr>
		<tr>
			<td><p>PMC4218929</p>
			</td>
			<td><p>Balb/c mice</p>
			</td>
			<td><p>4T1 murine breast tumor-bearing mice</p>
			</td>
			<td><p>4T1 murine breast tumor-bearing mice</p>
			</td>
		</tr>
		<tr>
			<td><p>PMC4038837</p>
			</td>
			<td><p>mice</p>
			</td>
			<td><p>4T1</p>
			</td>
			<td><p>4T1 murine breast cancer model</p>
			</td>
		</tr>
		<tr>
			<td><p>PMC6734012</p>
			</td>
			<td><p>Nude mice</p>
			</td>
			<td><p>N/A</p>
			</td>
			<td><p>athymic nude female mice</p>
			</td>
		</tr>
		<tr>
			<td><p>PMC5102673</p>
			</td>
			<td><p>Balb/c mice</p>
			</td>
			<td><p>not specified</p>
			</td>
			<td><p>Balb/c</p>
			</td>
		</tr>
		<tr>
			<td><p>PMC4550540</p>
			</td>
			<td><p>Balb/c mice</p>
			</td>
			<td><p>N/A</p>
			</td>
			<td><p>BALB/c</p>
			</td>
		</tr>
		<tr>
			<td><p>PMC3625170</p>
			</td>
			<td><p>ICR mice</p>
			</td>
			<td><p>not specified</p>
			</td>
			<td><p>ICR mice</p>
			</td>
		</tr>
		<tr>
			<td><p>PMC5197067</p>
			</td>
			<td><p>Nude mice</p>
			</td>
			<td><p>not specified</p>
			</td>
			<td><p>athymic nude mice</p>
			</td>
		</tr>
		<tr>
			<td><p>PMC3512544</p>
			</td>
			<td><p>Balb/c mice</p>
			</td>
			<td><p>N/A</p>
			</td>
			<td><p>BALB/c nude mice</p>
			</td>
		</tr>
		<tr>
			<td><p>PMC6462163</p>
			</td>
			<td><p>Nude mice</p>
			</td>
			<td><p>xenograft</p>
			</td>
			<td><p>nude, Balb/C</p>
			</td>
		</tr>
		<tr>
			<td><p>PMC4747947</p>
			</td>
			<td><p>Balb/c mice</p>
			</td>
			<td><p>not specified</p>
			</td>
			<td><p>Balb/c-nu</p>
			</td>
		</tr>
		<tr>
			<td><p>PMC7200226</p>
			</td>
			<td><p>Balb/c mice</p>
			</td>
			<td><p>4T1 tumor-bearing BALB/c mice</p>
			</td>
			<td><p>BALB/c</p>
			</td>
		</tr>
		<tr>
			<td><p>PMC5363536</p>
			</td>
			<td><p>Balb/c mice</p>
			</td>
			<td><p>not specified</p>
			</td>
			<td><p>BALB/c nu/nu</p>
			</td>
		</tr>
	</tbody>
</table>




**Downloading the data**: it is available as a supplementary material from the article text: https://ars.els-cdn.com/content/image/1-s2.0-S0169409X23000236-mmc1.xlsx
