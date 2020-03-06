class Rook extends Piece{
    constructor(position, source, type) {
        super(position,source,type);
    }

    getValidMoves() {
        
        let currentPos = Number(this.position);
        if (selectedPiece != this.position) {
            oldSelectedPiece = selectedPiece;
            selectedPiece = this.position;
            clearValidMoves();
            this.clean();
        }

        let movesUp = 90 - currentPos;

        //moves down
        for (let i = 10; i < movesUp; i += 10) {
            let option = currentPos + i;
            if (document.getElementById(option.toString()).src != ""){
                this.checkCapture(option);
                break;
            }
            if (option > 10)
                this.getMoveArray().push(option);
        }

        //moves up
        for (let i = 10; i < 90; i += 10) {
            let option = currentPos - i;
            if (option > 10 && document.getElementById(option.toString()).src == "")
                this.getMoveArray().push(option);
            if (option > 10 && document.getElementById(option.toString()).src != ""){
                this.checkCapture(option);
                break;
            }
        }

        //moves left
        for (let i = 1; i < 9; i += 1) {
            let option = currentPos - i;
            let mathRequirement1 = (Math.floor(currentPos / 10) * 10 + 9);
            let mathRequirement2 = (Math.floor(currentPos / 10) * 10);
            if (option > mathRequirement2 && option < mathRequirement1 && document.getElementById(option.toString()).src == "")
                this.getMoveArray().push(option);
            if (option > mathRequirement2 && option < mathRequirement1 && document.getElementById(option.toString()).src != ""){
                this.checkCapture(option);
                break;
            }
        }

        //moves right
        for (let i = 1; i < 9; i += 1) {
            let option = currentPos + i;
            let mathRequirement1 = (Math.floor(currentPos / 10) * 10 + 9);
            let mathRequirement2 = (Math.floor(currentPos / 10) * 10);
            if (option > mathRequirement2 && option < mathRequirement1 && document.getElementById(option.toString()).src == "")
                this.getMoveArray().push(option);
            if (option > mathRequirement2 && option < mathRequirement1 && document.getElementById(option.toString()).src != ""){
                this.checkCapture(option);
                break
            }
        }

        moveOptions = this.getMoveArray();
        this.highlightMoves(this.getMoveArray());
        
    }

    getNextValidMoves(Rook) {
        let NextMoveArray = new Array();
        let currentPos = Number(Rook.position);
        if (selectedPiece != Rook.position) {
            oldSelectedPiece = selectedPiece;
            selectedPiece = Rook.position;
            clearValidMoves();
            this.clean();
        }

        let movesUp = 90 - currentPos;

        //moves down
        for (let i = 10; i < movesUp; i += 10) {
            let option = currentPos + i;
            if (document.getElementById(option.toString()).src != "") {
                this.checkCapture(option);
                break;
            }
            if (option > 10)
                NextMoveArray.push(option);
        }

        //moves up
        for (let i = 10; i < 90; i += 10) {
            let option = currentPos - i;
            if (option > 10 && document.getElementById(option.toString()).src == "")
                NextMoveArray.push(option);
            if (option > 10 && document.getElementById(option.toString()).src != "") {
                this.checkCapture(option);
                break;
            }
        }

        //moves left
        for (let i = 1; i < 9; i += 1) {
            let option = currentPos - i;
            let mathRequirement1 = (Math.floor(currentPos / 10) * 10 + 9);
            let mathRequirement2 = (Math.floor(currentPos / 10) * 10);
            if (option > mathRequirement2 && option < mathRequirement1 && document.getElementById(option.toString()).src == "")
                NextMoveArray.push(option);
            if (option > mathRequirement2 && option < mathRequirement1 && document.getElementById(option.toString()).src != "") {
                this.checkCapture(option);
                break;
            }
        }

        //moves right
        for (let i = 1; i < 9; i += 1) {
            let option = currentPos + i;
            let mathRequirement1 = (Math.floor(currentPos / 10) * 10 + 9);
            let mathRequirement2 = (Math.floor(currentPos / 10) * 10);
            if (option > mathRequirement2 && option < mathRequirement1 && document.getElementById(option.toString()).src == "")
                NextMoveArray.push(option);
            if (option > mathRequirement2 && option < mathRequirement1 && document.getElementById(option.toString()).src != "") {
                this.checkCapture(option);
                break
            }
        }

        moveOptions = this.getMoveArray();
        var returnArray = NextMoveArray.concat(moveOptions);
        this.NextMove = returnArray;
        return returnArray;
    }
}