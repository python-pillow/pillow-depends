#!/bin/bash
# Use this script to create a tar.gz with rav1e vendored crates

RAV1E_VERSION=${RAV1E_VERSION:-$1}

if [ -z "$IS_DOCKER" ]; then
    DEPENDS_DIR=$(cd $(dirname $0) && pwd -P)

    if [ ! -e "$DEPENDS_DIR/rav1e-$RAV1E_VERSION.tar.gz" ]; then
        >&2 echo "Usage: rav1e-vendorize.sh VERSION"
        >&2 echo ""
        >&2 echo "Creates a tar.gz file with a vendor directory containing "
        >&2 echo "rav1e VERSION's dependencies."
        >&2 echo ""
        >&2 echo "VERSION must correspond to a file named rav1e-\$VERSION.tar.gz"
        exit 1
    fi

    docker run --rm \
        -v "$DEPENDS_DIR:/io" \
        -e RAV1E_VERSION=$RAV1E_VERSION \
        -e IS_DOCKER=1 \
        rustlang/rust:nightly-slim \
        /io/rav1e-vendorize.sh
else
    cd /tmp
    tar -zxvf /io/rav1e-$RAV1E_VERSION.tar.gz
    cd rav1e-$RAV1E_VERSION
    cargo vendor --versioned-dirs
    tar -a -cf /io/rav1e-vendor-$RAV1E_VERSION.tar.gz vendor
fi
