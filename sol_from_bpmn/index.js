const compiler = require("bpmn-sol");
const fs = require("fs");

fs.readFile("./diagram.bpmn", "utf8", function (err, contents) {
  console.log(contents);

  const xml = {
    bpmn: contents,
    name: "Sample_contract",
  };

  console.log("after calling readFile");

  const contract = compiler.compile(xml).then((contract, err) => {
    console.log(contract);


    fs.writeFileSync('./solfiles/diagram.sol', contract.Solidity)

    console.log(err)
  });
});
